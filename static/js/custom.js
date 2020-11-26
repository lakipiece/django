 // ���� Ÿ�Կ��� �� �� �ֵ��� format() �Լ� �߰�
 Number.prototype.format = function(){
    if(this==0) return 0;
 
    var reg = /(^[+-]?\d+)(\d{3})/;
    var n = (this + '');
 
    while (reg.test(n)) n = n.replace(reg, '$1' + ',' + '$2');
 
    return n;
};
 
// ���ڿ� Ÿ�Կ��� �� �� �ֵ��� format() �Լ� �߰�
String.prototype.format = function(){
    var num = parseFloat(this);
    if( isNaN(num) ) return "0";
 
    return num.format();
};


// ��¥ ��ȿ�� üũ
function isValidDate(param) {
	try
	{
		param = param.replace(/-/g,'');

		// �ڸ����� ����������
		if( isNaN(param) || param.length!=8 ) {
			return false;
		}
		 
		var year = Number(param.substring(0, 4));
		var month = Number(param.substring(4, 6));
		var day = Number(param.substring(6, 8));

		var dd = day / 0;

		 
		if( month<1 || month>12 ) {
			return false;
		}
		 
		var maxDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
		var maxDay = maxDaysInMonth[month-1];
		 
		// ���� üũ
		if( month==2 && ( year%4==0 && year%100!=0 || year%400==0 ) ) {
			maxDay = 29;
		}
		 
		if( day<=0 || day>maxDay ) {
			return false;
		}
		return true;

	} catch (err) {
		return false;
	}                       
};
	
		