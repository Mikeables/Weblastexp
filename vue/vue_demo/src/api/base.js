/*
*用于存放所有的api接口
*/
const base  ={
    baseUrl:'/api', // 使用代理
    login:'/user/login',  //登录
    get_menu:'/menu/menus/?type_=tree', //获取菜单
    get_menu_list:'/menu/menus/',
    get_users:'/user/users/', //获取用户列表
    get_user_by_id:'/user/user/',//根据id获取用户下信息
    add_user:'/user/users/',//添加用户
    edit_user:'/user/user/',//编辑用户信息
    delete_user:'/user/user/',              //删除用户
    rest_user_password:'/user/reset_pwd/', //重置用户密码
    get_roles:'/roles/' ,//获取角色列表
    del_role_menu:'/role/', //删除角色菜单
    set_menu:'/role/',
    get_category:'/categorys/',//获取分类信息
    add_category:'/categorys/',//添加分类
    get_attr_by_category:'/attributes/',//根据分类获取属性
    add_attr:'/attributes/',       //添加属性
    add_attr_value:'/attribute/',
    get_product_list:'/products/', //查询商品
    delete_product:'/product/', //删除商品
    upload_img:'/upload_img/', //上传图片
    add_product:'/products/', //添加商品
    get_orders:'/orders/', //获取订单列表
    get_express:'/expresses/',//获取物流信息
    get_cate_group:'/cate_grup/',//获取分类组
}


export default base