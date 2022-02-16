/* eslint-disable no-console */
(async () => {
  const { execa } = await import("execa");
  const fs = await import("fs");
  const { stdout: branch } = await execa("git", ["rev-parse", "--abbrev-ref", "HEAD"]);
  try {
    await execa("git", ["checkout", "--orphan", "gh-pages"]);
    // eslint-disable-next-line no-console
    console.log("Building started...");
    await execa("npm", ["run", "build"]);
    // Understand if it's dist or build folder
    const folderName = fs.existsSync("dist") ? "dist" : "build";
    await execa("git", ["--work-tree", folderName, "add", "--all"]);
    await execa("git", ["--work-tree", folderName, "commit", "-m", "gh-pages"]);
    console.log("Pushing to gh-pages...");
    await execa("git", ["push", "origin", "HEAD:gh-pages", "--force"]);
    await execa("git", ["checkout", "-f", branch]);
    await execa("git", ["branch", "-D", "gh-pages"]);
    console.log("Successfully deployed.");
  } catch (e) {
    // eslint-disable-next-line no-console
    console.log(e.message);
    process.exit(1);
  }
})();