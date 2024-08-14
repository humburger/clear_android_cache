import os, re

'''
removes destined cache folder which usually is full of annoying advertisements

CAUTION: used recursive function, so probably only good for small amount folder tree
'''

# CONST_DIRNAME = "/storage/emulated/0/Android/data/com.filemanager.exfile.explorer.exmanager/cache"
# CONST_DIR_SLASH = "/"
CONST_DIR_SLASH = "\\"
CONST_DIRNAME = "C:\\Users\\User\\Downloads\\ffmpeg-4.3-win64-static_ANDROID TESTING"
CONST_REGEX = ".*(cache|Cache).*"

def regEx_cache(dir):
	if re.search(CONST_REGEX, dir):
		print(dir)
		return 1 # regEx found
	else:
		return 0 # regEx not found


def remove_empty_dir(dir, regEx):
	if os.listdir(dir):
		# print("not empty " + dir)
		return 1
	else:
		# print("empty " + dir)
		if regEx == 2:
			os.rmdir(dir) # removes empty folder on sight
			# print("REMOVED DIR:\n" + dir)
		return 0

def dir_existence(dir, regEx):
	if os.path.exists(dir) and os.path.isdir(dir):
		# print(str(dir)) # show directory which exists
		return 0
	else:
		if regEx == 2:
			remove_file(dir) # removes non-folder on sight
		return 1

# recursive function so probably only good for small amount folder tree
def read_dir(dir_list, dir_slash, regEx):
	n_dir_list = os.listdir(dir_list)
	for dir in n_dir_list:
		next_dir = dir_list + dir_slash + dir

		if regEx == 0:
			regEx = regEx_cache(next_dir) # cache folder has been found
		elif regEx == 1:
			regEx = 2 # cache subfolders
		else:
			pass

		if dir_existence(next_dir, regEx) == 0:
			read_dir(next_dir, dir_slash, regEx)
			remove_empty_dir(next_dir, regEx)
		else:
			pass
	# print("script end")
	return 0

def remove_file(path):
	if os.path.exists(path): # checks if file exists before removal
		os.remove(path)
		# print("REMOVED FILE:\n" + path)
	else:
		pass
		
# main script
def empty_cf(dir, dir_slash, regEx):
	print("Chosen directory: "  + dir)
	# run script only if there are files and folders inside and folder is existing
	if os.path.exists(dir) and os.path.isdir(dir):
		if os.listdir(dir): 
			read_dir(dir, dir_slash, regEx)
		else:
			print("chosen folder is already empty")
			pass
	else:
		print("chosen folder is non-existent")
		pass

# __name__ guard // https://stackoverflow.com/a/419185
if __name__ == '__main__':
	empty_cf(CONST_DIRNAME, CONST_DIR_SLASH, 0)
	print("script 'empty_cache_folder' is running as main script")
else:
	print("script 'empty_cache_folder' is running as modular attachment")
	pass
