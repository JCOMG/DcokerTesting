
CI/CD
- 什麼是CI/CD -> Continue Integrate / Continue Deployment  
- 為什麼要有CI/CD -> 在開發大型專案的時候，可以自動測試跟部署，省時間
- CI/CD是要解決什麼問題 -> 節省時間，在develop小型開發的時候，可以手動檢查跟測試，但是features 或其他東西變多的時候就會很麻煩且耗時間
- 用來做CI/CD的工具有哪些 -> Jenkins, GitLab CI, Github actions

Docker
- 什麼是docker -> 一個抽象的詞彙，一個可以讓使用者在虛擬環境中開發、部署應用程式。
- 為什麼要有docker -> 今天我要開發一個東西，我使用的作業系統環境、語言版本可能跟其他team member用的不一樣，所以Docker可以確保我跟我的team member的環境same，不會因為我們的版本不同而不能使用。
- Docker是為了解決什麼問題 -> 解決環境版本的不同導致無法使用。

Github actions
- 什麼是github actions -> CI/CD 工具
- 

寫一支用來確認server是不是還活著的api GET /heath 回傳200, 要有unit test
Using postman to test it

![image](https://github.com/user-attachments/assets/fbfcdb1d-c201-4344-ad9b-3dc020f2f370)


用docker build image, 和用container把server跑起來
i create a image called my-flask-app and use container to run it 
![image](https://github.com/user-attachments/assets/aefe02c5-62c3-41ac-b3b1-46ba0a727b46)
![image](https://github.com/user-attachments/assets/c743637d-7a13-4fac-8cf1-8b1eb4bd617f)


加github actions進來, 當你發PR進main branch的時候會trgger github actions 去跑build和test

![image](https://github.com/user-attachments/assets/7197a165-0aaf-410a-8305-1892d1db9fc2)

我change branch called testing, change return "ok" -> return "okkkkkk"
and merge tigether 
