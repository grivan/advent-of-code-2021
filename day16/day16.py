from functools import reduce

class Reader:
    
    H2B = {
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111",
    }
    
    def __init__(self, hexinp):
        self.hexinp = hexinp
        self.bininp = "".join([self.H2B[x] for x in self.hexinp])
        self.version_sum = 0
        self.start = 0
        
    def read_packet(self):
        # print("Read Packet ", self.start)
        version = self.bininp[self.start:self.start+3]
        typeid = int(self.bininp[self.start+3:self.start+6], 2)
        self.start += 6        
        self.version_sum += int(version, 2)
        

        if typeid == 4:
            val = self.read_type4_literal()
        else:
            val = self.read_operator_packet(typeid)
        
        return val
        
    def read_operator_packet(self, typeid):
        # print("Reading Operator Packet: ", self.start)
        length_type_id = self.bininp[self.start]
        self.start+=1
        
        if length_type_id == '1':
            return self.read_operator_type1(typeid)
        elif length_type_id == '0':
            return self.read_operator_type0(typeid)
        else:
            print("ERROR!")
            
    def read_operator_type1(self, typeid):
        # print("Reading Operator Packet Type 1: ", self.start)
        num_packets = int(self.bininp[self.start:self.start+11], 2)
        self.start += 11
        packets = []
        while(num_packets > 0):
            packets.append(self.read_packet())
            num_packets -= 1
        return self.process_packets(packets, typeid)
    
    def read_operator_type0(self, typeid):
        # print("Reading Operator Packet Type 0: ", self.start)
        total_length = int(self.bininp[self.start:self.start+15], 2)
        self.start += 15
        packets = []
        max_read = self.start + total_length
        while(self.start < max_read):
            packets.append(self.read_packet())
        return self.process_packets(packets, typeid)
       
    def process_packets(self, packets, typeid):
        if typeid == 0:
            return sum(packets)
        elif typeid == 1:
            return reduce(lambda x,y: x*y, packets, 1)
        elif typeid == 2:
            return min(packets)
        elif typeid == 3:
            return max(packets)
        elif typeid == 5:
            return 1 if packets[0] > packets[1] else 0
        elif typeid == 6:
            return 1 if packets[0] < packets[1] else 0
        elif typeid == 7:
            return 1 if packets[0] == packets[1] else 0
        
    def read_type4_literal(self):
        # print("Reading Literal Packet: ", self.start)
        binlit = ""
        while(True):
            five = self.bininp[self.start:self.start+5]
            if five[0] == "1":
                binlit += five[1:5]
                self.start+=5
            elif five[0] == "0":
                binlit += five[1:5]
                self.start+=5
                break
            else:
                print("ERROR!")

        return int(binlit, 2)

# reader = Reader("8A004A801A8002F478")
# reader.read_packet()
# print("PART 1: "+ str(reader.version_sum), 16)

# reader = Reader("620080001611562C8802118E34")
# reader.read_packet()
# print("PART 1: "+ str(reader.version_sum), 12)

# reader = Reader("C0015000016115A2E0802F182340")
# reader.read_packet()
# print("PART 1: "+ str(reader.version_sum), 23)

# reader = Reader("A0016C880162017C3686B18A3D4780")
# reader.read_packet()
# print("PART 1: "+ str(reader.version_sum), 31)

INPUT = "day16/day16.in"
with open(INPUT) as infile:
    hexline = infile.readline().rstrip()
    reader = Reader(hexline)
    result = reader.read_packet()
    print("PART 1: "+ str(reader.version_sum))
    print("PART 2: "+ str(result))