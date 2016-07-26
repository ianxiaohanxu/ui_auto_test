#-*-coding:utf-8-*-
import json
from robot.utils import asserts
from robot.libraries.BuiltIn import BuiltIn

class Jsonto(object):
    u"""Json to object.

    """

    ROBOT_LIBRARY_DOC_FORMAT = 'text'
    ROBOT_LIBRARY_VERSION    = '0.2'

    def _index_to_int(self,index,empty_to_zero=False):
        if empty_to_zero and not index:
            return 0
        try:
            return int(index)
        except ValueError:
            raise ValueError("不能转换 '%s' 为整数." % index)

    def _index_error(self,list_,index):
        raise IndexError("Given index '%s' is out of the range 0-%d." % (index,len(list_)-1))

    def json_convert_to_object(self,str):
        u"""Convert Json format to object.

        Examples:
        | Json Convert To Object | [1,2,3,null,true] |        
        """

        return json.loads(str)

    def get_from_jsonArray(self,array,index):
        u"""get value from json string.

        Examples:
        | Get From Json List | [1,2,3,null,true] | 2 |
        """

        list_ = json.loads(array)

        try:
            return list_[self._index_to_int(index)]
        except IndexError:
            self._index_error(list_,index)

    def jsonArray_should_contain_value(self,array,value,msg=None):
        u"""json string should contain value.

        Examples:
        | jsonArray Should Contain Value | [1,2,3,null,true] | ${2} |
        """
        list_ = json.loads(array)
        
        if msg is None:
            msg = "列表没包含 %s." % value
        asserts.fail_unless(value in list_,msg)

    def jsonArray_should_not_contain_value(self,array,value,msg=None):
        u"""json string should not contain value.

        Examples:
        | jsonArray Should Not Contain Value | [1,2,3,null,true] | ${False} |
        """

        list_ = json.loads(array)
        if msg is None:
            msg = "列表包含了 %s." % value
        asserts.fail_if(value in list_,msg)

    def get_from_jsonObject(self,obj,key=None):
        u"""从json字符串obj中获指定key的值

        key可以由下列三种类型组成,如 /key/:index/key1:index1
        - /key
        - /:index
        - /key:index
        
        Examples:
        | Get From JsonObject | [[1,2,3],[4,5,6,{"k1":[7,8,9]}]] | /:1/:3/k1:1 |
        =>
        8
        """

        result = json.loads(obj)

        if not key:
            return result

        keys = (x for x in key.split("/") if x)

        for k in keys:
            kk = k.split(":")

            if len(kk) > 2:
                raise Exception(u'key: "%s" 参数填写错误！' % k)

            elif len(kk) > 1:
                if kk[0] != '':
                    result = result[kk[0]]

                if kk[1] != '':
                    idx = self._index_to_int(kk[1])
                    result = result[int(kk[1])]
            else:
                result = result[kk[0]]

        return result

    def get_length_from_json(self, obj, key=None):
        u"""获取json字符串obj中指定key的长度

        Examples:
        | Get Length From Json | [[1,2,3],[4,5,6,{"k1":[7,8,9]}]] | /:1/:3/k1 |
        =>
        3
        """

        o = self.get_from_jsonObject(obj, key)

        return len(o)

    def json_lenght_should_be(self, obj, key, length):
        u"""json字符串obj中指定key的长度应该为length

        Examples:
        | json lenght should be | [[1,2,3],[4,5,6,{"k1":[7,8,9]}]] | /:1/:3/k1 | 3 |

        """

        length = int(length)
        actual = self.get_length_from_json(obj, key)

        if actual != length:
            raise AssertionError("Length should be %d but is %d." % (length, actual))

    def json_value_should_equal_as_integers(self, obj, key, value):
        u"""如果json字符串obj中指定key的值和value的值转换为整型后不相等，则失败

        Examples:
        | json value should equal as integers | [[1,2,3],[4,5,6,{"k1":[7,8,9]}]] | /:1/:3/k1:7 | "8" |

        """
        first = self.get_from_jsonObject(obj, key)
        _builtin = BuiltIn()
        _builtin.should_be_equal_as_integers(first, value)

if __name__ == "__main__":

    obj = '[[1,2,3],[4,5,6,{"k1":{"k2":[7,8,9]}}]]'
    key = '/:1/:3/k1/k2'

    j = Jsonto()

    print j.get_from_jsonObject(obj, key)
    print j.get_length_from_json(obj, key)
    print j.json_value_should_equal_as_integers(obj, '/:1/:3/k1/k2:1', 8)