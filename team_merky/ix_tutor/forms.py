from django import forms
from datetime import datetime

class S2STestForm(forms.Form):
	TYPES_CHOICES = [('imp', 'bidreq.imp.'),
					( 'ext', 'bidreq.ext.')]
	EXT_TYPE_CHOICES = [('string', 'string'),
						('number', 'number')]
	AD_UNIT_CHOICES = [('728x90', '728x90'),
						('300x250', '300x250'), 
						('250x250', '250x250'), 
						('336x280', '336x280'), 
						('200x200', '200x200'), 
						('300x600', '300x600'), 
						('320x480', '320x480'), 
						('160x600', '160x600'), 
						('300x100', '300x100'), 
						('120x600', '120x600')]

	partnerID = forms.IntegerField(label="Partner ID:", 
		required=True, min_value=1, max_value=999)
	bidUrl = forms.URLField(label="Bidding Endpoint:",
		required=True, help_text="The endpoint we'll be sending test bid requests to.")
	partnerCode = forms.CharField(label="Company Name:", required=True, max_length=255,
		help_text="Son a ma beech")
	
	######################### IMPEXT (DYNAMIC) MAPPINGS #########################################
	partnerRequestParam = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	impExtValue = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")

	partnerRequestParam2 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam2 = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	impExtValue2 = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType2 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")

	partnerRequestParam3 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam3 = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenfRTB Request")
	impExtValue3 = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType3 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")	
	#############################################################################################
	
	######################### SITE (DYNAMIC) MAPPINGS #########################################
	partnerRequestParam4 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam4 = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	siteValue = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType4 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")

	partnerRequestParam5 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam5 = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	siteValue2 = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType5 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")

	partnerRequestParam6 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	pegasusRequestParam6 = forms.CharField(label="PEGasus Request Parameter:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenfRTB Request")
	siteValue3 = forms.CharField(label="PEGasus Request Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType6 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
		required=False, help_text="Indicates data type this value will be in OpenRTB request")	
	#############################################################################################
	
	########################## STATIC MAPPINGS ##################################################
	types = forms.ChoiceField(label="Mapping Type:", choices=TYPES_CHOICES,
		required=False, help_text="Indicates where the targeting data will be place in OpenRTB request")
	partnerRequestParam7 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	value = forms.CharField(label="Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType7 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
			required=False, help_text="Indicates data type this value will be in OpenRTB request")

	types2 = forms.ChoiceField(label="Mapping Type:", choices=TYPES_CHOICES,
		required=False, help_text="Indicates where the targeting data will be place in OpenRTB request")
	partnerRequestParam8 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	value2 = forms.CharField(label="Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType8 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
			required=False, help_text="Indicates data type this value will be in OpenRTB request")

	types3 = forms.ChoiceField(label="Mapping Type:", choices=TYPES_CHOICES,
		required=False, help_text="Indicates where the targeting data will be place in OpenRTB request")
	partnerRequestParam9 = forms.CharField(label="PARtner Request Parameter:", 
		required=False, max_length=255, 
		help_text="Value (site ID, placement ID, etc) you will use to target your inventory.")
	value3 = forms.CharField(label="Value:", 
		required=False, max_length=255,
		help_text="Where you'd like your site/placement/etc id in the OpenRTB Request")
	externalType9 = forms.ChoiceField(label="Data Type:", choices=EXT_TYPE_CHOICES,
			required=False, help_text="Indicates data type this value will be in OpenRTB request")	
	#############################################################################################
	
	insecure = forms.BooleanField(label="Receive Insecure Traffic", 
		required=False, help_text="OpenRTB field imp.secure = 0", initial=True)
	secure = forms.BooleanField(label="Receive Secure Traffic",
	 required=False, help_text="OpenRTB field imp.secure = 1")
	adUnits = forms.MultipleChoiceField(label="Test Ad Units", required=True,
		help_text="Ad Units we are to send you in testing", choices=AD_UNIT_CHOICES)
	useDollars = forms.BooleanField(label="Bid in Dollars", required=False)
	sendSeat = forms.BooleanField(label="Send seatbid.seat value", required=False)
	buyeruid = forms.CharField(label="BuyerUID:", 
		required=False, max_length=255, 
		help_text="To be placed in user.buyeruid field of OpenRTB Requests")
	ip = forms.CharField(label="IP Address:", required=False, max_length=255,
		help_text="To be placed in the device.ip field of OpenRTB Requests")
	page = forms.URLField(label="Page Field:", required=False, help_text="page field of request")
	def __init__(self, *args, **kwargs):
		super(S2STestForm, self).__init__(*args, **kwargs)
		extraDynamicImp = ['partnerRequestParam2', 'pegasusRequestParam2', 'impExtValue2', 'externalType2',
				'partnerRequestParam3', 'pegasusRequestParam3', 'impExtValue3', 'externalType3']
		extraDynamicSite = ['partnerRequestParam5', 'pegasusRequestParam5', 'impExtValue5', 'externalType5',
				'partnerRequestParam6', 'pegasusRequestParam6', 'impExtValue6', 'externalType6']
		extraStatic = ['types2', 'partnerRequestParam8', 'value2', 'externalType8',
				'types3', 'partnerRequestParam9', 'value3', 'externalType9',]
		for field in self.fields:
			if field in extraDynamicImp:
				self.fields[field].widget.attrs.update({'class':'required extraDynamicImp'})
			elif field in extraDynamicSite:
				self.fields[field].widget.attrs.update({'class':'required extraDynamicSite'})
			elif field in extraStatic:
				self.fields[field].widget.attrs.update({'class':'required extraStatic'})
			else:
				self.fields[field].widget.attrs.update({'class':'required'})

	def clean(self):
		# ill validate 
		inv_types = ['secure', 'insecure']
		cleaned_data = super(S2STestForm, self).clean()
		one_true = False
		for inv_type in inv_types:
			if cleaned_data.get(inv_type, False):
				one_true = True
				break
		if (not one_true):
			self.add_error("secure", forms.ValidationError(('You must select at least one inventory type for testing.'), code='no_inv_type'))
		
		# Validate that for every 
		type_validation = {"externalType":"impExtValue",
							"externalType2":"impExtValue2",
							"externalType3":"impExtValue3",
							"externalType4":"siteValue",
							"externalType5":"siteValue2",
							"externalType6":"siteValue3",
							"externalType7":"value",
							"externalType8":"value2",
							"externalType9":"value3"}
		for key in type_validation.keys():
			if cleaned_data.get(key, False) == 'number':
				try:
					print key
					print cleaned_data[key]
					print cleaned_data[type_validation[key]]
					int(cleaned_data[type_validation[key]])
				except ValueError:
					self.add_error(type_validation[key], forms.ValidationError(('Specified type number for value but input a string.'), code='type_mismatch'))

		#######################################################################
		# CONFIGURATION CONSOLIDATION
		# 
		# Gathers all inputs from widgets IF partnerRequestParam is populated
		# ASSUMES other fields are populated if partnerRequestX is
		#######################################################################
		dynamic_map_checks = ["partnerRequestParam", "partnerRequestParam2", "partnerRequestParam3",
			"partnerRequestParam4", "partnerRequestParam5", "partnerRequestParam6"]
		dynamic_map_inserts = {
	    	"requestParams": dynamic_map_checks,
	    	"dataTypes": ["externalType", "externalType2", "externalType3",
	    		"externalType4", "externalType5", "externalType6"],
	    	"impExtValues": ["impExtValue", "impExtValue2", "impExtValue3",
	    		"siteValue", "siteValue2", "siteValue3"],
	    	"values": ["pegasusRequestParam", "pegasusRequestParam2", "pegasusRequestParam3",
	    		"pegasusRequestParam4", "pegasusRequestParam5", "pegasusRequestParam6"]
	    }
		static_map_checks = ["partnerRequestParam7", "partnerRequestParam8", "partnerRequestParam9"]
		static_map_inserts = {
	    	"allTypes": ["types", "types2", "types3"],
	    	"requestParams": ["partnerRequestParam7", "partnerRequestParam8", "partnerRequestParam9"],
	    	"dataTypes": ["externalType7", "externalType8", "externalType9"],
	    	"values": ["value", "value2", "value3"]
	    }

		consolidated_conf_names = ["allTypes", "impExtValues", "requestParams", "dataTypes", "values"]
		for name in consolidated_conf_names:
			cleaned_data[name] = ""
		

		for dynamic_check_index in range(len(dynamic_map_checks)):
			x = cleaned_data.get(dynamic_map_checks[dynamic_check_index], "")
			if x:
				# first 3 partner request params are for impext mappings and
				# the next 3 are for site type mappings (see form declaration)
				if dynamic_check_index < 3:
					cleaned_data["allTypes"] += 'impExt,'
				else:
					cleaned_data["allTypes"] += 'site,'
				for formdata_insert_key in dynamic_map_inserts.keys():
					cleaned_data[formdata_insert_key] += str(cleaned_data.get(dynamic_map_inserts[formdata_insert_key][dynamic_check_index])) + ","

		for static_check_index in range(len(static_map_checks)):
			x = cleaned_data.get(static_map_checks[static_check_index], "")
			if x:
				for formdata_insert_key in static_map_inserts.keys():
					cleaned_data[formdata_insert_key] += str(cleaned_data.get(static_map_inserts[formdata_insert_key][static_check_index])) + ","

		for name in consolidated_conf_names:
			cleaned_data[name] = cleaned_data[name].rstrip(",")
		return cleaned_data

class DSPUserForm(forms.Form):

	username = forms.CharField(label="Username", required=True, max_length=255)
	pw = forms.CharField(label="Password", required=True, max_length=255, widget=forms.PasswordInput())
	conf_pw = forms.CharField(label="Confirm Password", required=True, max_length=255, widget=forms.PasswordInput())
	expiry = forms.DateTimeField(required=True, input_formats=["%Y-%m-%d %H:%M:%S",], initial=datetime.now())

	def __init__(self, *args, **kwargs):
		super(DSPUserForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class':'required'})

	def clean(self):
		cleaned_data = super(DSPUserForm, self).clean()
		if cleaned_data.get("pw") != cleaned_data.get("conf_pw"):
			self.add_error('pw', forms.ValidationError(('Password fields do not match.'), code='mismatch'))
		return cleaned_data
