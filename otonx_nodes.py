# wildcard trick is taken from pythongossss's
# I found it in Impact Pack's nodes
class AnyType(str):
	def __ne__(self, __value: object) -> bool:
		return False

any_type = AnyType("*")

class OTX_VersatileMultipleInputs:

	def __init__(self):
		pass

	@classmethod
	def INPUT_TYPES(self):
		return {
			"required": {
				"value_1": ("STRING", {"default": "", "multiline": True}),
				"valuetype_1": (list(('int', 'float', 'string')),),
				"value_2": ("STRING", {"default": "", "multiline": True}),
				"valuetype_2": (list(('int', 'float', 'string')),),
				"value_3": ("STRING", {"default": "", "multiline": True}),
				"valuetype_3": (list(('int', 'float', 'string')),),
				"value_4": ("STRING", {"default": "", "multiline": True}),
				"valuetype_4": (list(('int', 'float', 'string')),),
				"value_5": ("STRING", {"default": "", "multiline": True}),
				"valuetype_5": (list(('int', 'float', 'string')),),
			},
		}
	RETURN_TYPES = (any_type, any_type, any_type, any_type, any_type,)
	RETURN_NAMES = ("value_1", "value_2", "value_3", "value_4", "value_5")

	FUNCTION = "pass_parameters"

	CATEGORY = "OtonxPack"

	def pass_parameters(self, value_1, value_2, value_3, value_4, value_5, valuetype_1, valuetype_2, valuetype_3, valuetype_4, valuetype_5):
		# Convert value_1 based on valuetype_1
		if valuetype_1 == "INT":
			value_1 = int(value_1)
		elif valuetype_1 == "FLOAT":
			value_1 = float(value_1)
		elif valuetype_1 == "STRING":
			value_1 = str(value_1)

		# Convert value_2 based on valuetype_2
		if valuetype_2 == "INT":
			value_2 = int(value_2)
		elif valuetype_2 == "FLOAT":
			value_2 = float(value_2)
		elif valuetype_2 == "STRING":
			value_2 = str(value_2)

		# Convert value_3 based on valuetype_3
		if valuetype_3 == "INT":
			value_3 = int(value_3)
		elif valuetype_3 == "FLOAT":
			value_3 = float(value_3)
		elif valuetype_3 == "STRING":
			value_3 = str(value_3)

		# Convert value_4 based on valuetype_4
		if valuetype_4 == "INT":
			value_4 = int(value_4)
		elif valuetype_4 == "FLOAT":
			value_4 = float(value_4)
		elif valuetype_4 == "STRING":
			value_4 = str(value_4)

		# Convert value_5 based on valuetype_5
		if valuetype_5 == "INT":
			value_5 = int(value_5)
		elif valuetype_5 == "FLOAT":
			value_5 = float(value_5)
		elif valuetype_5 == "STRING":
			value_5 = str(value_5)
		return value_1, value_2, value_3, value_4, value_5


class OTX_KSampler_Feeder:

	def __init__(self):
		pass

	@classmethod
	def INPUT_TYPES(self):
		return {
			"required": {
				"noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
				"steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
				"base_steps_portion": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 1.0, "step": 0.1, "display": "number"}),
			},
		}

	RETURN_TYPES = ("INT","INT","FLOAT","INT",)

	RETURN_NAMES = ("noise_seed", "steps", "cfg", "base_end_at_step",)

	FUNCTION = "pass_parameters"

	CATEGORY = "OtonxPack"

	def pass_parameters(self, base_steps_portion, noise_seed, steps, cfg):
		base_end_at_step = int(steps * base_steps_portion)
		return noise_seed, steps, cfg, base_end_at_step