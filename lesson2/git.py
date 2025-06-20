''' 
настройки 
    git config --global user.email my_email@gmail.com
    git config --global user.name “name”
    git config --list

начало работы
    git init - инициализировать папку для работы с гит
    git clone <url> - скопировать репозиторий с гитхаба - инициализация уже не нужна

просмотр состояния
    git status

добавить в стэйдж
    git add *.txt
    git add some_file.txt
    git add .


создать коммит - зафиксировать изменения
    git commit -m "some commit"

список коммитов
    git log
    git log --oneline - краткая запись
    git log -p - подробно с изменениями 
    git log --pretty=format:"%h - %an, %ar : %s"
    git log --all --graph --oneline


отмена изменений
    git restore file или . - отменить изменения без коммита
    git revert hash - отменяет изменения создавая еще один коммит. Таким образом есть история
    git reset hash - отмена коммита как будто не существовало, нельзя если уже отправлен на github


ветки
    git branch - список веток
    git branch vetka2 - создать новую ветку
    git checkout  name - переключить 
    git checkout -b b3 - переключить с созданием
    git branch -d <name> - удалить
    git push --set-upstream origin <branch_name> - скопировать в хаб и назначить удаленную ветку
    git push -u origin <branch_name> - назначить удаленную ветку - тоже самое

слияние веток
    git merge hotfix - влить hotfix в текущую

соединить с удаленным  репозиторием
    git remote - список удаленных
    git remote add <name> <url> - name обычно делают - origin
    git remote show <name>
    git remote remove <name>


залить на гитхаб
    git push 
    git push <remote-name> <branch-name>
    
забрать изменения с гитхаба
    git fetch - загружает но не модифицирует
    git pull - загрузка с гитхаб




'''

