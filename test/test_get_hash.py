from southy import LocalRepository


repo = LocalRepository('https://github.com/Wakayama-SocSEL/southy.git')
print(repo.findall_commit_hashes())
