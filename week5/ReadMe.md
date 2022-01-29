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

要求三:

1.
	
	1.1輸入 => INSERT INTO `member` VALUES(NULL,'test','test','test',100,NOW()); 按下ENTER，成功後出現以下畫面 (建立test帳號 VALUES分別對應TABLE內容)

![image](https://github.com/joesound/wehelp-assignments/blob/371752e9ab709626ef7aabd2a34dbb87acfb47f7/week5/static/mysqltest.png)

	1.2輸入 => 
			INSERT INTO `member` VALUES(NULL,'google','google','google',120,NOW());
			
			INSERT INTO `member` VALUES(NULL,'amazon','amazon','amazon',20,NOW());
			
			INSERT INTO `member` VALUES(NULL,'tsmc','tsmc','tsmc',40,NOW()); 
			
			INSERT INTO `member` VALUES(NULL,'Netflix','Netflix','Netflix',30,NOW()); 

按下ENTER，成功後出現以下畫面 (分別建立 四筆資料)

![image](https://github.com/joesound/wehelp-assignments/blob/b4128872cdc52724098f618c6938eab33e310fec/week5/static/mysqladd4.png)

2.輸入 => SELECT * FROM `member`; 按下ENTER，成功後出現以下畫面 
	  
![image](https://github.com/joesound/wehelp-assignments/blob/b4128872cdc52724098f618c6938eab33e310fec/week5/static/mysqladd4.png)

3.輸入 => SELECT * FROM `member` ORDER BY `time` DESC; 按下ENTER，成功後出現以下畫面 (排序按照時間近到遠) 

![image](https://github.com/joesound/wehelp-assignments/blob/44c88f9a007b9c9c2e7e468c4686e9235f896f18/week5/static/mysqlorderbydesc.png)

4.輸入 => SELECT * FROM `member` ORDER BY `time` DESC Limit 1,3; 按下ENTER，成功後出現以下畫面 (第 2 ~ 4 共三筆資料，並按照 time 欄位)

![image](https://github.com/joesound/wehelp-assignments/blob/71a3fefe620e7fd8808228fdf9d231b290120c20/week5/static/mysqlchoose24.png)

5.輸入 => SELECT * FROM `member` WHERE `username`='test'; 按下ENTER，成功後出現以下畫面 (test 的會員資料)

![image](https://github.com/joesound/wehelp-assignments/blob/6ac364be900d6cb7feb325761b0982e575a0ec44/week5/static/mysqltestdata.png)

6.輸入 => SELECT `username`, `password` FROM `member` WHERE `username`='test'; 按下ENTER，成功後出現以下畫面 (欄位 username 是 test、且欄位 password 也是 test 的資料)

![image](https://github.com/joesound/wehelp-assignments/blob/4d8cbb43d94abba385d68b1bcb95202446c6cda5/week5/static/mysqltesttest.png)

7.輸入 => UPDATE `member` AS `men`, (SELECT `id` FROM `member` WHERE `username`='test') AS `test_id` SET `name`='test2' WHERE `men`.`id`=`test_id`.`id`;

按下ENTER，成功後出現以下畫面 (將test會員的name欄位改成test2)

![image](https://github.com/joesound/wehelp-assignments/blob/745fb3da41cf3f43dbca2ce94abd49681e17ec64/week5/static/mysqlupdate.png)

要求四:

1.輸入 => SELECT COUNT(`username`) FROM `member`; 按下ENTER，成功後出現以下畫面 (總共有幾筆會員資料)

![image](https://github.com/joesound/wehelp-assignments/blob/b7cf16fe1a7ff6db5396b155441737c99f329aad/week5/static/mysqlcount.png)

2.輸入 => SELECT SUM(`follower_count`) FROM `member`; 按下ENTER，成功後出現以下畫面 (計算follower_count 欄位的總和)

![image](https://github.com/joesound/wehelp-assignments/blob/b7cf16fe1a7ff6db5396b155441737c99f329aad/week5/static/mysqlsum.png)

3.輸入 => SELECT AVG(`follower_count`) FROM `member`; 按下ENTER，成功後出現以下畫面 (計算follower_count 欄位的平均數)

![image](https://github.com/joesound/wehelp-assignments/blob/b7cf16fe1a7ff6db5396b155441737c99f329aad/week5/static/mysqlavg.png)


要求五:

1.輸入 => CREATE TABLE `message` (
          
	  `id` bigint PRIMARY KEY AUTO_INCREMENT,
	  
	  `member_id` bigint NOT NULL ,
	  
	  `content` varchar(255) NOT NULL,
	  
	  `time` datetime NOT NULL DEFAULT NOW(),
	  
	  FOREIGN KEY (`member_id`) REFERENCES `member`(`id`)
	
    );
    
按下ENTER，成功後出現以下畫面 (新增message TABLE)

![image](https://github.com/joesound/wehelp-assignments/blob/6d388b948ae3d505d4b0b784ddb8c1315de383ef/week5/static/mysqlmessage.png)

2.輸入 =>  
	
	INSERT INTO `message` VALUES(NULL,1,'very good',NOW());

	INSERT INTO `message` VALUES(NULL,2,'nice!',NOW());

	INSERT INTO `message` VALUES(NULL,3,'awesome',NOW());

	INSERT INTO `message` VALUES(NULL,4,'like',NOW());

	INSERT INTO `message` VALUES(NULL,1,'like',NOW());

	INSERT INTO `message` VALUES(NULL,1,'good',NOW());

	INSERT INTO `message` VALUES(NULL,1,'well done',NOW());
	
按下ENTER，成功後出現以下畫面 (新增留言)

![image](https://github.com/joesound/wehelp-assignments/blob/d5ce06e50056c817aab0ae451e4a9af7dea0f5aa/week5/static/mysqladdcomment.png)

3.輸入 => SELECT `message`.`content`, `member`.`name` FROM `message` INNER JOIN `member` ON `message`.`member_id`=`member`.`id`; 按下ENTER，成功後出現以下畫面 (取得所有留言，包含留言者會員的姓名)

![image](https://github.com/joesound/wehelp-assignments/blob/0ffe3a081cc9e2620ac36c315ad498318df61da7/week5/static/mysqljoin1.png)
