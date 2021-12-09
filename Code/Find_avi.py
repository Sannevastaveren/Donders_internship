import os




def find_downsampled():
  all = []
  for root, dirs, files in os.walk("/content/drive/My Drive/Stage/"):
      for file in files:
          if file.endswith(".avi"):
            if 'downsampled' in file:
              all.append(os.path.join(root, file))
  return all
            
def find_finished_total():  
  total = 0
  finished = 0
  for root, dirs, files in os.walk("/content/drive/My Drive/Stage/"):
      for file in files:
          if file.endswith(".avi"):
            if 'downsampled' not in file:
              total += 1
              file_z = file.replace('.', 'downsampled.')
              if os.path.join(root, file_z) in all:
                finished += 1
  return finished, total

def downsample_stuff(all, finished, total):
  for root, dirs, files in os.walk("/content/drive/My Drive/Stage/"):
      for file in files:
          if file.endswith(".avi"):
            old_file = os.path.join(root, file)
            already_in = False      
            if 'downsampled' not in file:
              file_z = file.replace('.', 'downsampled.')
              if os.path.join(root, file_z) in all:
                  already_in = True
                  #print(os.path.join(root, file))
              if already_in is False:
                  old_file = os.path.join(root, file)
                  file_l = file.split('.')
                  file_l[1] = 'downsampled'
                  file_l.append('.avi')
                  file = ''.join(file_l)
                  new_file =  os.path.join(root, file)
                  !ffmpeg -i "$old_file" -filter:v scale=-1:256 -c:a copy "$new_file"
                  finished += 1
                  print(total, '/', finished)
                  os.remove(old_file)
              if already_in is True:
                  os.remove(old_file)

all = find_downsampled()
finished, total = find_finished_total()
downsample_stuff(all, finished,total)
print(total, '/', finished)
print(total, '/', len(all))
# everything downsampled is "done" so -- all = done
# everything not downsampled is to do -- so create list with that
# everything everything is all avi videos -- so create list with that

# total = all non downsampled videos
# all = all downsampled videos
# finished = all already downsampled videos