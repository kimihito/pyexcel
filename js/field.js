var ItemField = { 
    currentNumber : 1, 
    itemTemplate : '<h3>商品登録__count__</h3>' +'品名:<input type="text" name="name" size="30" maxlength="1000"/><br />\n価格:<input type="text" name="price" size="30" maxlength="1000" /><br />\n個数:<input type="text" name="piece" size="2" maxlength="100" />個<br />\n',
    add : function(){ 
        this.currentNumber++; 
        var field = document.getElementById('item' + this.currentNumber); 
        var newItem = this.itemTemplate.replace(/__count__/mg, this.currentNumber);
        field.innerHTML = newItem; 

        var nextNumber = this.currentNumber + 1;
        var new_area = document.createElement("div");
        new_area.setAttribute("id", "item" + nextNumber);
        field.appendChild(new_area);
    },
    remove : function() {
        if (this.currentNumber == 1) {return;}

        var field = document.getElementById('item' + this.currentNumber);
        field.removeChild(field.lastChild);
        field.innerHTML = '';

        this.currentNumber--;
    }
}


