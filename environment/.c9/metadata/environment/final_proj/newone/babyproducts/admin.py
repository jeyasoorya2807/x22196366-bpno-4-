{"filter":false,"title":"admin.py","tooltip":"/final_proj/newone/babyproducts/admin.py","undoManager":{"mark":28,"position":28,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":26},"action":"insert","lines":["from django.contrib import admin","# Register your models here.","from .models import Movie","admin.site.register(Movie)"],"id":3}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":25},"action":"remove","lines":["Movie"],"id":4}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["b"],"id":5},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["a"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["b"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["y"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["p"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["r"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["d"],"id":6},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["u"]},{"start":{"row":2,"column":29},"end":{"row":2,"column":30},"action":"insert","lines":["c"]},{"start":{"row":2,"column":30},"end":{"row":2,"column":31},"action":"insert","lines":["t"]},{"start":{"row":2,"column":31},"end":{"row":2,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":25},"action":"remove","lines":["Movie"],"id":7}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["b"],"id":8},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["a"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["b"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["y"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["p"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["d"],"id":9},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["u"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["c"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["t"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":33},"action":"remove","lines":["from django.contrib import admin","# Register your models here.","from .models import babyproducts","admin.site.register(babyproducts)"],"id":10}],[{"start":{"row":0,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["from django.contrib import admin","from .models import BabyProduct  # Use CamelCase for the model name","","admin.site.register(BabyProduct)  # Register the model with the admin site",""],"id":11}],[{"start":{"row":1,"column":34},"end":{"row":1,"column":67},"action":"remove","lines":[" Use CamelCase for the model name"],"id":12},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":["#"]}],[{"start":{"row":3,"column":34},"end":{"row":3,"column":74},"action":"remove","lines":["# Register the model with the admin site"],"id":13},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"remove","lines":[" "]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["B"],"id":17}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["b"],"id":18}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":[" "],"id":19},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":[" "]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["s"],"id":20}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["P"],"id":21}],[{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["p"],"id":22}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["B"],"id":23}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["b"],"id":24}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["b"],"id":25},{"start":{"row":3,"column":20},"end":{"row":3,"column":32},"action":"insert","lines":["babyproducts"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["a"],"id":26},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["b"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["y"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["P"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["r"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["o"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["d"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["u"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["c"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["t"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["b"],"id":27}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["B"],"id":28}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["s"],"id":29}],[{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"remove","lines":["s"],"id":30},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"remove","lines":["t"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"remove","lines":["c"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"remove","lines":["u"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["d"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["o"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":["r"],"id":31},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["p"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["y"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["b"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["a"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["b"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["B"],"id":32},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["a"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["b"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["y"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["p"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"],"id":33},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["o"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["d"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["u"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["c"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":0},"end":{"row":4,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1699462190273,"hash":"0c4ccc87d4e9a04a110b9a09ebd2551633b460f2"}