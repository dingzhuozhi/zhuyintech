import pandas as pd
df=pd.read_csv("网页数据.txt",sep="\t")
txt_form=r"美国pce/美国核心PCE物价指数月率"
df.to_csv(r"{}.csv".format(txt_form),index=False)
