# Setup new git repo
### <span style="color:orange;">**Create new repo on [github.com](http://github.com)**</span>

Open the web browser login github.com

New the repo named e.g. aqs8server
### <span style="color:orange;">**Local source code prepare**</span>

Download and install git: https://git-scm.com/downloads
```bash
# download git and setup
git --version
git config --global --list
git config --global user.name "xxx"
git config --global user.email "xxx.email.com"
git config --global user.password "xxx"
```
### <span style="color:orange;">**Upload your first commit:**</span>

```bash
# Create local Git repo:
cd \Projects\\
git init draw [proj folder]
# if folder not exist, it will create new folder
# and hidden folder aqs\.git will be created
cd draw
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/karock5345/luckdraw.git
git push -u origin main
# ! [rejected]        main -> main (fetch first)
# error: failed to push some refs to 'https://github.com/karock5345/djchannels4.git'
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.

# change 'origin' -> other remote name e.g. 'remote-rvd'
```
### <span style="color:orange;">**Commit new version to github**</span>

Open vscode -> open the project -> Source Control (Crtl + Shift + G) -> add some text on "Message" e.g. fixed bug xxx -> ... -> commit -> commit all
