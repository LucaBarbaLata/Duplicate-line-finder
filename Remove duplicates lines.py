import hashlib
def main():
    input_file = "rockyou.txt"
    output_file = "out.txt"
    completed_hash = set()
    output_file = open(output_file, "w")
    for line in open(input_file,"r"):
        hashValue = hashlib.md5(line.strip().encode('utf-8')).hexdigest()
        if hashValue not in completed_hash:
            output_file.write(line)
            completed_hash.add(hashValue)
    output_file.close()
if __name__ == "__main__":
    main()