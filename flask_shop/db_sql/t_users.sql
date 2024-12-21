-- 插入 t_users 表的数据
INSERT INTO t_users (name, pwd, nick_name, phone, email, role_id, create_time, update_time) VALUES ('admin', '123456', '管理员', '1234567890', 'admin@example.com', 1, NOW(), NOW());
INSERT INTO t_users (name, pwd, nick_name, phone, email, role_id, create_time, update_time) VALUES ('user1', '123456', '用户1', '1234567891', 'user1@example.com', 3, NOW(), NOW());
INSERT INTO t_users (name, pwd, nick_name, phone, email, role_id, create_time, update_time) VALUES ('user2', '123456', '用户2', '1234567892', 'user2@example.com', 3, NOW(), NOW());
