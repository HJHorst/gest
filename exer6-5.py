text = "X-DSPAM-Confidence:    0.8475";
semi = text.find(":")
getal = float((text[semi+1:len(text)]).strip())
print getal