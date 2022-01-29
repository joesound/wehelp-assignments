要求一:
1.下載mysql安裝檔(https://dev.mysql.com/downloads/windows/installer/8.0.html)

2.安裝mysql，並設定root帳號密碼

3.打開環境變數，將mysql加入Path(C:\Program Files\MySQL\MySQL Server 8.0\bin)

4.以系統執行者開啟CMD，輸入 => net start mysql80 (依照版本輸入不同數字)，成功後出現以下畫面

![image](https://github.com/joesound/wehelp-assignments/blob/0809547182c061b35cff82651f6e05e51a4b5f2f/week5/static/mysqlstart.png)

5.輸入 => mysql -h localhost -u root -p ，按下ENTER，會出現輸入密碼，成功後出現以下畫面

![image](https://github.com/joesound/wehelp-assignments/blob/1d4a61478abebf92c667250b6ebcc22e2ed9113d/week5/static/mysqlpaaword.png)

6.輸入 => password，按下ENTER，成功後出現以下畫面

![image](https://github.com/joesound/wehelp-assignments/blob/b2d213cd0f35638edaf6a43f0cb4ba0ba9e6cb4a/week5/static/mysqlsigin.png)

要求二:

1.輸入 => SHOW DATABSES; 按下ENTER，成功後出現以下畫面 (由於尚未新建website資料庫，所以只有預設的資料庫存在)

![image](https://github.com/joesound/wehelp-assignments/blob/8e1a71596a64dbb8bcb81c3e96a7857f634abd6e/week5/static/mysqldefalt.png)

2.輸入 => CREATE DATABASE `website`; 按下ENTER，成功後出現以下畫面(新建website資料庫)

![image](https://github.com/joesound/wehelp-assignments/blob/521efbae11a4ba571938def01d24345fb49d805b/week5/static/mysqlwebsite.png)

3.輸入 => USE `website`; 按下ENTER，成功後出現以下畫面(選擇資料庫)

![image](https://github.com/joesound/wehelp-assignments/blob/40ebd1ac94514f3f9267d15bc4401d616a2ad713/week5/static/mysqlchoosedatabase.png)

4.輸入 => CREATE TABLE `member` (  
          
          `id` bigint PRIMARY KEY AUTO_INCREMENT,
          
          `name` varchar(255) NOT NULL,
          
          `username` varchar(255) NOT NULL,
    
          `password` varchar(255) NOT NULL,
          
          `follower_count` int DEFAULT 0,
	        
          `time` datetime NOT NULL DEFAULT NOW()
          
    ); 按下ENTER，成功後出現以下畫面 (建立member table，並按照需求設定預設值及資料型態)
    
![image](https://github.com/joesound/wehelp-assignments/blob/fa2602e138c3c0ccadaeeda55b0b331ab73eeecf/week5/static/mysqlmember.png)

5.輸入 => SHOW TABLES; 按下ENTER，成功後出現以下畫面(看到資料庫中存在的TABLE)

![image](https://github.com/joesound/wehelp-assignments/blob/390598205479c2752b69ae802a25308a52a7eb37/week5/static/mysqlshowtables.png)
