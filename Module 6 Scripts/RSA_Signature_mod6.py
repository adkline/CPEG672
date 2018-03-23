import random, binascii
from Crypto.PublicKey import RSA

gen_key = RSA.generate(2048, e = 65537)

public_key = gen_key.publickey().exportKey("PEM") 
private_key = gen_key.exportKey("PEM") 

print public_key
print private_key

m = "I solemnly swear to learn applied cryptography. Even though there are not enough graded assignments to incentivize the needed hours I will: 1) work problems 2) ask questions 3) ponder start-ups 4) think in a paranoid fashion 5) get it done without excuse"
m_hex = binascii.hexlify(m)
m_int = int(m_hex,16)



#rsa_testing.txt
#n = 26555818315545122301751077409629760500790210636296793926879845240069872644050318548968747450975923374086618133646202779328212405546865480653303590632169334112878633669624512229297696797360067756813978948205570051552263127846544972571287276960030031994746497707882240313288768903519594589104516126968527171676366450738215301668502277433014417584892914597589136316743029303210499962554092428395742206395738107309626685196600750144684648963103253218768736759994227331026666424455363286772554192011373369892846246879200485731555242824742067999927217639857625760336477346836832273663065853301031265586567985935942565879131
e = 65537
#d = 4238833260584364929713261528329598922727106725457386839023605918128247214999319198937425684493631603770696130370217240254397210345694184859151454317456145446920417272959427841229888554513994671773670350751155352080324466795897080398373990330330563875322994835316784654734177815580793734785271574899946026563667165806832543266008847837627450616876438633777005247525809871955138580929461125795511679682436473426500451674707796935081409922391771474864789047232298471173750944653038370730858845205594966539074664402686899622216968281521916286649134624375380992918026182652220605804275398454506666841466761703424242490289 

sigma = pow(m_int,d,n)

print sigma


### Verify

Verify = pow(sigma,e,n)

print "Verify is" , Verify
print " M as int is",  m_int






