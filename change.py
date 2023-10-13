replacement_map = {
    "D:/desktop/file/HP_all":   # 原本的文字
    "D:/desktop/file/HP_all_CLAHE",  #修改後的文字
}

# 讀取記事本內容.txt
file_path = "here.txt"  # 換成你的檔案，記得打上路徑，然後路徑\/用哪個上網查
with open(file_path, 'r') as file: # read模式讀取
    file_content = file.read() #讀檔案進來的意思

# 文字做替換
for original_str, target_str in replacement_map.items():
    file_content = file_content.replace(original_str, target_str)

# 將修改後的內容存回檔案裡
with open(file_path, 'w') as file: # write 模式寫入，是會整個覆蓋的那種，a 才是加在最後一筆後面
    file.write(file_content)

print("更改完成")
