import { defaultLocation } from "@vueuse/core";
import axios from "../utils/request.js";//引入封装好的axios
import base from "./base.js" //引入接口域名列表

const api = {
    /*
    *登录功能
    */
    login(user) {
      return axios.post(`${base.baseUrl}${base.login}`, {
        name: user.name,
        pwd: user.pwd
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
    },
   /*login(user) {
      return axios.post(`${base.baseUrl}${base.login}`, `name=${user.name}&pwd=${user.pwd}`, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
    },*/
//    logout(){
//     return axios.get(base.baseUrl+base.logout)
//    }
   get_menu(params){
    return axios.get(base.baseUrl+base.get_menu,params)
   },
   get_menu_list(params){
      return axios.get(base.baseUrl+base.get_menu_list,params)
   },
   get_user_list(params){
      return axios.get(base.baseUrl+base.get_users,params)
   },
   add_user(params){
      return axios.post(base.baseUrl+base.add_user,params)
   },
   get_user_by_id(id){
      return axios.get(base.baseUrl+base.get_user_by_id+id+'/')
   },
   edit_user(id,params){
      return axios.put(base.baseUrl+base.edit_user+id+'/',params)
   },
   delete_user(id){
      return axios.delete(base.baseUrl+base.delete_user+id+'/')
  },
  reset_user_password(id){
      return axios.get(base.baseUrl+base.rest_user_password+id+'/')
  },
  get_roles(params){
   return axios.get(base.baseUrl+base.get_roles,params)
  },
  del_role_menu(rid,mid){
   return axios.get(base.baseUrl+base.del_role_menu+rid+'/'+mid+'/')
   },
   set_menu(rid,params){
      return axios.post(base.baseUrl+base.set_menu+rid+'/',params)
   },
   get_category(level){
      return axios.get(base.baseUrl+base.get_category+'?level='+level)
   },
   add_category(params){
      return axios.post(base.baseUrl+base.add_category,params)

   },
   get_attr_by_category(cid,_type){
      return axios.get(base.baseUrl+base.get_attr_by_category+'?cid='+cid+'&_type='+_type)

   },
   add_attribute (params){
      return axios.post(base.baseUrl+base.add_attr, params)
  },
  add_attr_value(id,params){
   return axios.put(base.baseUrl+base.add_attr_value+id+'/',params)
  },
  get_product_list(name){
   if(name){
      return axios.get(base.baseUrl+base.get_product_list+'?name='+name)
   }else{
      return axios.get(base.baseUrl+base.get_product_list)
   }
  },
  delete_product(id){
   return axios.delete(base.baseUrl+base.delete_product+id+'/')
  },
  add_product(params){
   return axios.post(base.baseUrl+base.add_product, params)
},
get_orders(params){
   return axios.get(base.baseUrl+base.get_orders, params)
},
get_express(id){
   return axios.get(base.baseUrl+base.get_express+id+'/')
},
get_category_group(){
   return axios.get(base.baseUrl+base.get_cate_group)
}
}
export default api