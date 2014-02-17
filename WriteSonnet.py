import sys
from SonnetWriter import SonnetWriter

if __name__ == '__main__':
    writer = SonnetWriter()
    print "Initializing..."
    writer.Initialize("Sonnets.txt")
    print "Initialized"
    print 
    print "Analyzing..."
    writer.AnalyzeText()
    print "Analyzed"
    print 
    print "Generating..."
    writer.WriteSonnet()
    print "\nGenerated"
    print 
    print "My magnum opus: "
    print 
    writer.Print(True)
    writer.Print(False)
    print(writer.GetPrintableSonnet("", "{1} ", "</ br>\n"))

