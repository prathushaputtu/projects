from rembg import remove

input_path = "btsv.jpg"
output_path = "btsv_downloaded.jpg"

with open(input_path, "rb") as i:
 with open(output_path, "wb") as o:
  input = i.read()
  output = remove(input)
  o.write(output)