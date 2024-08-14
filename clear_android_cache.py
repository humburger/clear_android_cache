import os, empty_cache_folder, re

'''
removes destined cache folder which usually is full of annoying advertisements

'''

# CONST_DIRNAME = "/storage/emulated/0/Android/data/com.filemanager.exfile.explorer.exmanager/cache"
# CONST_DIR_SLASH = "/"
CONST_DIR_SLASH = "\\"
CONST_DIRNAME = "C:\\Users\\User\\Downloads\\ffmpeg-4.3-win64-static_ANDROID TESTING"
CONST_DIR_LIST = os.listdir(CONST_DIRNAME)

# will get array with listdir and recursively with read_dir removes dir and subfolders with files
def read_folder_list(dir, dir_slash):
	
	dir_list = os.listdir(dir)
	for dir_incr in dir_list:
		next_dir = dir + dir_slash + dir_incr

		if empty_cache_folder.dir_existence(next_dir, 0) == 0:
			empty_cache_folder.read_dir(next_dir, dir_slash, 0) # recursive folder clearance and removal
		else:
			pass

	print("script end")
	return 0

# probably this code can be used from empty_cache_folder
def clear_ac(dir, dir_slash):
	print("Chosen directory: "  + dir)
	# run script only if there are files and folders inside and folder is existing
	if os.path.exists(dir) and os.path.isdir(dir):
		if os.listdir(dir): 
			# empty_cache_folder.read_dir(dir, dir_slash, 0)
			read_folder_list(dir, dir_slash)
			pass
		else:
			print("chosen folder is already empty")
			pass
	else:
		print("chosen folder is non-existent")
		pass

# __name__ guard // https://stackoverflow.com/a/419185
if __name__ == '__main__':
	clear_ac(CONST_DIRNAME, CONST_DIR_SLASH)
	print("script 'clear_android_cache' is running as main script")
else:
	print("script 'clear_android_cache' is running as modular attachment")
	pass
