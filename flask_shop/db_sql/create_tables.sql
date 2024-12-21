-- 创建 t_category 表
CREATE TABLE t_category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    level INT,
    pid INT,
    FOREIGN KEY (pid) REFERENCES t_category(id)
);

-- 创建 t_menu 表
CREATE TABLE t_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL UNIQUE,
    level INT,
    path VARCHAR(32),
    pid INT,
    FOREIGN KEY (pid) REFERENCES t_menu(id)
);

-- 创建 t_roles 表
CREATE TABLE t_roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL UNIQUE,
    `desc` VARCHAR(128)
);

-- 创建 t_attribute 表
CREATE TABLE t_attribute (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    _type ENUM('static', 'dynamic'),
    cid INT,
    val VARCHAR(255),
    FOREIGN KEY (cid) REFERENCES t_category(id)
);

-- 创建 t_product 表
CREATE TABLE t_product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(512) NOT NULL,
    price FLOAT,
    number INT,
    introduce TEXT,
    big_img VARCHAR(255),
    small_img VARCHAR(255),
    state INT,
    is_promote INT,
    hot_number INT,
    weight INT,
    cid_one INT,
    cid_two INT,
    cid_three INT,
    FOREIGN KEY (cid_one) REFERENCES t_category(id),
    FOREIGN KEY (cid_two) REFERENCES t_category(id),
    FOREIGN KEY (cid_three) REFERENCES t_category(id)
);

-- 创建 t_roles_menus 表
CREATE TABLE t_roles_menus (
    role_id INT,
    menus_id INT,
    FOREIGN KEY (role_id) REFERENCES t_roles(id),
    FOREIGN KEY (menus_id) REFERENCES t_menu(id)
);

-- 创建 t_users 表
CREATE TABLE t_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(32) NOT NULL UNIQUE,
    pwd VARCHAR(128),
    nick_name VARCHAR(32),
    phone VARCHAR(11),
    email VARCHAR(32),
    role_id INT,
    create_time DATETIME,
    update_time DATETIME,
    FOREIGN KEY (role_id) REFERENCES t_roles(id)
);

-- 创建 t_order 表
CREATE TABLE t_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    price FLOAT,
    number INT,
    pay_status INT,
    is_send INT,
    FOREIGN KEY (uid) REFERENCES t_users(id)
);

-- 创建 t_picture 表
CREATE TABLE t_picture (
    id INT AUTO_INCREMENT PRIMARY KEY,
    path VARCHAR(255),
    pid INT,
    FOREIGN KEY (pid) REFERENCES t_product(id)
);

-- 创建 t_product_attr 表
CREATE TABLE t_product_attr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pid INT,
    aid INT,
    val VARCHAR(256),
    _type ENUM('static', 'dynamic'),
    FOREIGN KEY (pid) REFERENCES t_product(id),
    FOREIGN KEY (aid) REFERENCES t_attribute(id)
);

-- 创建 t_express 表
CREATE TABLE t_express (
    id INT AUTO_INCREMENT PRIMARY KEY,
    oid INT,
    update_time VARCHAR(256),
    content VARCHAR(256),
    FOREIGN KEY (oid) REFERENCES t_order(uid)
);

-- 创建 t_order_detail 表
CREATE TABLE t_order_detail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    oid INT,
    pid INT,
    number INT,
    price FLOAT,
    total_price FLOAT,
    FOREIGN KEY (oid) REFERENCES t_order(id),
    FOREIGN KEY (pid) REFERENCES t_product(id)
);