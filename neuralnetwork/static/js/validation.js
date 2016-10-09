$.fn.validateInteger = function(errMsg, errLocation) {
	var value = this.val();
	var re = /^[0-9]+$/; // /^-?[1-9]\d*$/
	if(re.test(value)){
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};

$.fn.validatePositiveNum = function(errMsg, errLocation) {
	var value = this.val();
	var re = /^\d+(\.\d+)?$/; // /^-?[1-9]\d*$/99999.99
	var b = false;
	if(re.test(value)){
		var n = parseFloat(value);
		if(n >= 0){
			b=true;
		}
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
	return true;
};

$.fn.validate = function(errMsg, errLocation) {
	var value = this.val();
	if (value != null && value.length > 0) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};


$.fn.checkedCode = function(errMsg, errLocation) {
	var b = false;
	var value = this.val();
	var name = this.attr("name");
	$.ajax( {
		url : "VerifyCodeAction.action?" + name + "=" + value,
		dataType : "json",
		async : false,
		success : function(data) {
			if (data) {
				errLocation.text("");
				b = true;
			} else {
				errLocation.text(errMsg);
			}
		}
	});
	return b;
};

$.fn.adminPwdReset = function (url) {
	var b = false;
	
	$.ajax({url:url, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}  	
	}});
	return b;
};

$.fn.deleteAdmin = function (id) {
	var b = false;
	$.ajax({url:"deleteAdmin.action" + "?" + "idForAdminDel" + "=" + id, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}  	
	}});
	return b;
};

$.fn.deleteRole = function (id) {
	var b = false;
	$.ajax({url:"deleteRole.action" + "?" + "idForRoleDel" + "=" + id, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}  	
	}});
	return b;
};

$.fn.remote = function (url, errorMsg, errorCtn) {
	var b = false;
	var value = this.val();
	var name = this.attr("name");
	//alert(value);
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
		if (data) {
			$(errorCtn).text("");
			b = true;
		} else {
			$(errorCtn).text(errorMsg);
		}
	}});
	return b;
};

$.fn.remoteTrainingAndTest = function (url) {
	var b = false;
	//alert(url);
	$.ajax({url:url, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}
	}});
	return b;
};

$.fn.remotePost = function (url, errorMsg, errorCtn) {
	var b = false;
	var value = this.val();
	var name = this.attr("name");
	//alert(value);
	$.ajax({url:url, type:"post", data:name + "=" + value, dataType:"json", async:false, success:function (data) {
		if (data) {
			$(errorCtn).text("");
			b = true;
		} else {
			$(errorCtn).text(errorMsg);
		}
	}});
	return b;
};

$.fn.remoteDelete = function (id) {
	//alert("remoteDelete");
	var url = "accountDeleteAction.action";
	var b = false;
	$.ajax({url:url + "?" + "id" + "=" + id, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}
	}});
	return b;
};

$.fn.remoteDeleteService = function (id) {
	//alert("remoteDelete");
	var url = "serviceDeleteAction.action";
	var b = false;
	$.ajax({url:url + "?" + "id" + "=" + id, dataType:"json", async:false, success:function (data) {
		if (data) {
			b = true;
		}
	}});
	return b;
};

$.fn.remotePwdChange = function (url, jueryLoginName, errorMsg, errorCtn) {
	var b = false;
	var value = this.val();
	var name = this.attr("name");
	var valueLoginName = jueryLoginName.val();
	var nameLoginName = jueryLoginName.attr("name");
	//alert(url + "?" + name + "=" + value + "&" + nameLoginName + "=" + valueLoginName);
	$.ajax({url:url + "?" + name + "=" + value + "&" + nameLoginName + "=" + valueLoginName, dataType:"json", async:false, success:function (data) {
		if (data) {
			$(errorCtn).text("");
			b = true;
		} else {
			$(errorCtn).text(errorMsg);
		}
	}});
	return b;
};

$.fn.remoteValidateMainIDC = function (url, errorMsg, errorCtn) {
	var b = false;
	var value = this.val();
	var name = this.attr("name");
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
		if (data.ok) {
			$(errorCtn).text("");
			b = true;
		} else {
			$(errorCtn).text(errorMsg);
		}
	}});
	return b;
};


$.fn.remoteRecommemderId = function (url) {
	var b;
	var value = this.val();
	var name = this.attr("name");
	//alert(url + "?" + name + "=" + value);
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
		b = data;
	}});
	return b;
};

$.fn.remoteAccount = function (url) {
	var b;
	var value = this.val();
	var name = this.attr("name");
	//alert(url + "?" + name + "=" + value);
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
		b = data;
	}});
	return b;
};

$.fn.remoteGenerateBirth = function (url) {
	var b;
	var value = this.val();
	var name = this.attr("name");
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
			b = data;
	}});
	return b;
};

$.fn.remoteUpdate = function (url, errorMsg, errorCtn) {
	var b = false;
	var value = this.val();
	var name = "name";
	//var name = this.attr("name");
	alert(url + "?" + name + "=" + value);
	$.ajax({url:url + "?" + name + "=" + value, dataType:"json", async:false, success:function (data) {
		if (data) {
			//alert("ok");
			$(errorCtn).text("");
			b = true;
		} else {
			//alert("not ok");
			$(errorCtn).text(errorMsg);
		}
	}});
	return b;
};

$.fn.range = function(min, max, errMsg, errLocation){
	var value = this.val();
	if (value != null && value.length >=min && value.length <=max) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}	
};

$.fn.numberLenthRange = function(min, max, errMsg, errLocation){
	var value = this.val();
	var re = /^\d+$/;
	if(!re.test(value)){
		errLocation.text(errMsg);
		return false;
	}
	if (value != null && value.length >=min && value.length <=max) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}	
};

$.fn.intRange = function(min, max, errMsg, errLocation){ 
	var value = this.val();
	var re = /^[1-9]\d*$/; // /^-?[1-9]\d*$/
	var b = false;
	if(re.test(value)){
		var n = parseInt(value);
		if(n>=min&&n<=max){
			b=true;
		}
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};

$.fn.floatRange = function(min, max, errMsg, errLocation){ 
	var value = this.val();
	var re = /^\d+(\.\d+)?$/; // /^-?[1-9]\d*$/99999.99
	var b = false;
	if(re.test(value)){
		var n = parseFloat(value);
		if(n >= min && n <= max){
			b=true;
		}
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
	return true;
};

$.fn.certainNoLengthFormat = function(length, errMsg, errLocation){ 
	var value = this.val();
	var re = /^\d+$/; // /^-?[1-9]\d*$/
	var b = false;
	if(re.test(value)){
		if(value.length == length){
			b=true;
		}
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};

$.fn.certainIPFormat = function(errMsg, errLocation){ 
	var value = this.val();
	var re = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])(\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])){3}$/; // /^-?[1-9]\d*$/
	var b = false;
	if(re.test(value)){	
		b=true;	
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};


$.fn.telephoneNoLengthFormat = function(length, errMsg, errLocation){ 
	var value = this.val();
	var re = /^\d+$/; // /^-?[1-9]\d*$/
	var b = false;
	if(re.test(value)){
		if(value.length <= length){
			b=true;
		}
	}
	if (b) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
};

$.fn.validateTheSameValue = function(jqueryObj, errMsg, errLocation){
	var value1 = this.val();
	var value2 = jqueryObj.val();
	if (value1==value2) {
		errLocation.text("");
		return true;
	} else {
		errLocation.text(errMsg);
		return false;
	}
	
};
