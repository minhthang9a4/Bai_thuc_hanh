class Lipstick:
    def __init__(self, tenson, mausac, chatson, xuatsu, muithom):
        self.mausac = mausac
        self.chatson = chatson
        self.tenson = tenson
        self.xuatsu = xuatsu
        self.muithom = muithom
    def sudung(self, mucdich):
        return "{} sẽ có {}".format(self.tenson,mucdich) 
    def khinao(self):
        return"{} thường được dùng trong mùa đông".format(self.mausac)
    def chatluong(self):
       return"{} son giữ màu tốt ".format(self.tenson)
glossy = Lipstick("Glossy","Đỏ rượu","son bóng","Hàn Quốc","mùi hoa hồng")
blackrouge = Lipstick("Black Rouge","màu đỏ"," son lì ","Hàn Quốc","mùi kem")
print(glossy.sudung("chất dưỡng"))
print(glossy.khinao())
print(blackrouge.chatluong())



