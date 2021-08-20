# python
creat new repository:
	echo "# python" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git branch -M main
	git remote add origin git@github.com:zhang757/python.git
	git push -u origin main

push an existing repository:
	git remote add origin https://github.com/zhang757/python.git
	git branch -M main
	git push -u origin main
	
	
九十天的token令牌：
	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 

更改命令语句：
git remote set-url origin https://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@github.com/zhang757/python.git
