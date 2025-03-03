CHD
===

A bot which detects website changes

## For developers

Init database:

```sql
create database chd_db;
ALTER DATABASE chd_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER 'chd_db_user'@'localhost';
GRANT ALL PRIVILEGES ON chd_db.* To 'chd_db_user'@'localhost';
alter user 'chd_db_user'@'localhost' identified by '__chd';
flush privileges;
```
