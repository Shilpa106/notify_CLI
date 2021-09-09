import click
from click.decorators import option
from click.termui import prompt
import click_config_file
from click_didyoumean import DYMGroup
import sqlite3

conn = sqlite3.connect('data1.db')
c = conn.cursor()


# ********************************************
# a_budget_amount=specicific amount
# if a_amount_spent<50%:
#     	print(budget is underamount)


# CREATE TABLE t_shops (
#     a_id        INT(11)         NOT NULL AUTO_INCREMENT,
#     a_name      VARCHAR(255)    NOT NULL,
#     a_online    BOOLEAN         NOT NULL,
#     PRIMARY KEY (a_id)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# *************************************
# CREATE TABLE t_budgets (
#     a_shop_id       INT(11)         NOT NULL REFERENCES t_shops (a_id),
#     a_month         DATE            NOT NULL,
#     a_budget_amount DECIMAL(10,2)   NOT NULL,
#     a_amount_spent  DECIMAL(10,2)   NOT NULL,
#     PRIMARY KEY (a_shop_id, a_month)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# ********************************************
def create_table_t_shops():
    	#  ID INT PRI
		# cursor.execute("CREATE TABLE salesman2(salesman2_id n(5), name char(30), city char(35), commission decimal(7,2));")

    	c.execute('CREATE TABLE IF NOT EXISTS shoptable(a_id INT NOT NULL PRIMARY KEY ,a_name VARCHAR(255) NOT NULL,a_online  BOOLEAN NOT NULL);')
def create_table_t_budgets():
    	c.execute('CREATE TABLE IF NOT EXISTS budgettable(a_shop_id INT(11) NOT NULL REFERENCES t_shops(a_id),a_month DATE NOT NULL,a_budget_amount DECIMAL(10,2)   NOT NULL, a_amount_spent  DECIMAL(10,2)   NOT NULL,PRIMARY KEY (a_shop_id, a_month));')


def add_data_shoptable(a_id,a_name,a_online):
    	# c.execute('INSERT INTO budgettable(a_id,a_name,a_online) VALUES (?,?,?)',(a_id,a_name,a_online))
		# conn.commit()

		c.execute("""
		INSERT INTO shoptable VALUES(1,"Steve McQueen", 1);
		INSERT INTO shoptable VALUES(2, "Fashion Quasar",0);
		INSERT INTO shoptable VALUES(3,"As Seen On Sale",1);
		INSERT INTO shoptable VALUES(4,"H&R", 0);
		INSERT INTO shoptable VALUES(5,"Meow Meow", 1);
		INSERT INTO shoptable VALUES(6,"Dole & Cabbage",   0);
		INSERT INTO shoptable VALUES(7,"George Manly", 1);
		INSERT INTO shoptable VALUES(8,"Harrison Ford", 1);
		""",(a_id,a_name,a_online))

		# c.execute('INSERT INTO shoptable VALUES((1,"Steve McQueen",1),(2, "Fashion Quasar",0),(3,"As Seen On Sale",1),(4,"H&R", 0),(5,"Meow Meow", 1),(6,"Dole & Cabbage",   0), (7,"George Manly", 1), (8,"Harrison Ford", 1))',(a_id,a_name,a_online))
		conn.commit()

def add_data_budgettable(a_shop_id,a_month,a_budget_amount,a_amount_spent):
    	c.execute("""
		INSERT INTO budgettable VALUES(1, '2020-06-01', 930.00, 725.67);
		INSERT INTO budgettable VALUES(2, '2020-06-01', 990.00, 886.63);
		INSERT INTO budgettable VALUES(3, '2020-06-01', 650.00, 685.91);
		INSERT INTO budgettable VALUES(4, '2020-06-01', 740.00, 746.92);
		INSERT INTO budgettable VALUES(5, '2020-06-01', 630.00, 507.64);
		INSERT INTO budgettable VALUES(6, '2020-06-01', 640.00, 946.32);
		INSERT INTO budgettable VALUES(7, '2020-06-01', 980.00, 640.16);
		INSERT INTO budgettable VALUES(8, '2020-06-01', 790.00, 965.64);


        INSERT INTO budgettable VALUES(1, '2020-07-01', 960.00, 803.67);
		INSERT INTO budgettable VALUES(2, '2020-07-01', 670.00, 715.64);
		INSERT INTO budgettable VALUES(3, '2020-07-01', 890.00, 580.81);
		INSERT INTO budgettable VALUES(4, '2020-07-01', 590.00, 754.93);
		INSERT INTO budgettable VALUES(5, '2020-07-01', 870.00, 505.12);
		INSERT INTO budgettable VALUES(6, '2020-07-01', 700.00, 912.30);
		INSERT INTO budgettable VALUES(7, '2020-07-01', 990.00, 805.15);
		INSERT INTO budgettable VALUES(8, '2020-07-01', 720.00, 504.25);


		""",(a_shop_id,a_month,a_budget_amount,a_amount_spent))
    	# c.execute('INSERT INTO budgettable(a_shop_id,a_month,a_budget_amount,a_amount_spent) VALUES ((1, "2020-06-01", 930.00, 725.67),(2, "2020-06-01", 990.00, 886.63), (3, "2020-06-01", 650.00, 685.91),(4, "2020-06-01", 740.00, 746.92),(5, "2020-06-01", 630.00, 507.64),(6, "2020-06-01", 640.00, 946.32),(7, "2020-06-01", 980.00, 640.16),(8, "2020-06-01", 790.00, 965.64),(1, "2020-07-01", 960.00, 803.67),(2, "2020-07-01", 670.00, 715.64),(3, "2020-07-01", 890.00, 580.81),(4, "2020-07-01", 590.00, 754.93),(5, "2020-07-01", 870.00, 505.12),(6, "2020-07-01", 700.00, 912.30),(7, "2020-07-01", 990.00, 805.15),(8, "2020-07-01", 720.00, 504.25))',(a_shop_id,a_month,a_budget_amount,a_amount_spent))
		# conn.commit()



def view_all_budget():
	c.execute('SELECT * FROM budgettable')
	data = c.fetchall()
	print(data)
	# for row in data:
	# 	print(row)
	return data

	

def send_notification():
    pass

def shop_offline():
    	pass

# def get_single_note(a_id):
# 	c.execute('SELECT * FROM shoptable WHERE a_id="{}"'.format(a_id))
# 	data = c.fetchall()
# 	return data

# def get_note_by_Shop_id(a_shop_id):
# 	c.execute('SELECT * FROM budgettable WHERE Shop_id="{}"'.format(a_shop_id))
# 	data = c.fetchall()
# 	return data

# 	# get_note_by_

# def get_note_by_author(author):
# 	c.execute('SELECT * FROM budgettable WHERE author="{}"'.format(author))
# 	data = c.fetchall()
# 	return data
 

# def get_note_by_msg(message):
# 	c.execute("SELECT * FROM budgettable WHERE message like '%{}%'".format(message))
# 	data = c.fetchall()
# 	return data

# def edit_note_author(author,new_author):
# 	c.execute('UPDATE budgettable SET author ="{}" WHERE author="{}"'.format(new_author,author))
# 	conn.commit()
# 	data = c.fetchall()
# 	return data

# def edit_note_title(title,new_title):
# 	c.execute('UPDATE budgettable SET title ="{}" WHERE title="{}"'.format(new_title,title
# 		))
# 	conn.commit()
# 	data = c.fetchall()
# 	return data


# def edit_note_msg(message,new_message):
# 	c.execute('UPDATE budgettable SET title ="{}" WHERE title="{}"'.format(new_message,message
# 		))
# 	conn.commit()
# 	data = c.fetchall()
# 	return data

# def delete_shop(title):
# 	c.execute('DELETE FROM budgettable WHERE title="{}"'.format(title))
# 	conn.commit()


@click.group(cls=DYMGroup)
@click.version_option(version='0.01',prog_name='termipad')
def main():
	""" Termipad : A simple budget taking CLI  
	"""
	pass


@main.command()
@click.option('--a_id','-a',prompt=True)
@click.option('--a_name','-n',prompt=True)
@click.option('--a_online','-on',prompt=True)
@click_config_file.configuration_option()
def add_shop(a_id,a_name,a_online):
	""" Add A New Shop
	eg. python budget_mgmt.py add-note --author Jesse --title "Simple Terminal budget" --message "A simple note taking cli"
	eg. python budget_mgmt.py add-note -a JCharis -t "Best budget" -msg "This is secret"
	"""
	click.echo("==============================")
	click.secho('Shop_id:: {}'.format(a_id),fg='white',bg='blue')
	click.secho('Shop_name:: {}'.format(a_name),fg='white',bg='yellow')
	click.secho('online_shop:: {}'.format(a_online),fg='blue')

	click.echo("========Summary===============")
	from terminaltables import AsciiTable

	shop_details = [
		['budget Info','Details'],
		['a_id:',a_id],
		['a_name:',a_name],
		['a_online:',a_online],
	
	]
	create_table_t_shops()
	# create_table()
	add_shop(a_id,a_name,a_online)
	table1 = AsciiTable(shop_details)

	click.echo(table1.table)
	click.secho('Saved Shop Details To DataBase',fg='blue')


# *******************************************budget***************************************************************
# CREATE TABLE t_budgets (
#     a_shop_id       INT(11)         NOT NULL REFERENCES t_shops (a_id),
#     a_month         DATE            NOT NULL,
#     a_budget_amount DECIMAL(10,2)   NOT NULL,
#     a_amount_spent  DECIMAL(10,2)   NOT NULL,
#     PRIMARY KEY (a_shop_id, a_month)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
@main.command()
@click.option('--a_shop_id','-id',prompt=True)
@click.option('--a_month','-m',prompt=True)
@click.option('--a_budget_amount','-bam',prompt=True)
@click.option('--a_amount_spent','-aaspent',prompt=True)
@click_config_file.configuration_option()

# *********************
# def add_note(author,title,message):
#     	""" Add A New Notes
# 	eg. python termipad.py add-note --author Jesse --title "Simple Terminal Notes" --message "A simple note taking cli"
# 	eg. python termipad.py add-note -a JCharis -t "Best Notes" -msg "This is secret"
# 	"""
# 	click.echo("==============================")
# 	click.secho('Author:: {}'.format(author),fg='white',bg='blue')
# 	click.secho('Title:: {}'.format(title),fg='white',bg='yellow')
# 	click.secho('Message:: {}'.format(message),fg='blue')

# 	click.echo("========Summary===============")
# 	from terminaltables import AsciiTable
# 	user_notes = [
# 		['Notes Info','Details'],
# 		['Title:',title],
# 		['Author:',author],
# 		['Message Length:',len(message)],
	
# 	]
# 	create_table()
# 	add_data(author,title,message)
# 	table1 = AsciiTable(user_notes)

# 	click.echo(table1.table)
# 	click.secho('Saved Notes To DataBase',fg='blue')

# *********************
def add_budget(a_shop_id,a_month,a_budget_amount,a_amount_spent):
	""" Add A New budget
	eg. python budget_mgmt.py add-note --author Jesse --title "Simple Terminal budget" --message "A simple note taking cli"
	eg. python budget_mgmt.py add-note -a JCharis -t "Best budget" -msg "This is secret"
	"""
	click.echo("==============================")
	click.secho('Shop_id:: {}'.format(a_shop_id),fg='white',bg='blue')
	click.secho('Month:: {}'.format(a_month),fg='white',bg='blue')
	click.secho('budget_amount:: {}'.format(a_budget_amount),fg='white',bg='yellow')
	click.secho('amount_spent:: {}'.format(a_amount_spent),fg='blue')

	click.echo("========Summary===============")
	from terminaltables import AsciiTable
	budget_details = [
		['budget Info','Details'],
		['a_shop_id:',a_shop_id],
		['a_month:',a_month],
		['a_budget_amount:',a_budget_amount],
		['a_amount_spent:',a_amount_spent]
	
	]
	create_table_t_budgets()
	# create_table()
	add_budget(a_shop_id,a_month,a_budget_amount,a_amount_spent)
	table1 = AsciiTable(budget_details)

	click.echo(table1.table)
	click.secho('Saved Shop Details To DataBase',fg='blue')
# ****************************************************************************************************************

# @main.command()
# @click.option('--Shop_id','-id',prompt=True)
# def shop_note(a_id):
# 	""" View Note By Title 
	
# 	eg.	python budget_mgmt.py view-note --title "Best budget"
# 	eg.  python budget_mgmt.py view-note -t "Best budget"
# 	"""
# 	click.secho("Searched For {}".format(a_id),bg='blue')
# 	from terminaltables import AsciiTable
# 	result = get_single_note(a_id)
# 	table1 = AsciiTable(result)
# 	click.echo(table1.table)

# *******************************************************************************************************

# @main.command()
# @click.argument('number')
# @click.option('--by','-b',default='Shop_id')
# def search(number,by):
# 	""" Search Note By Options [Title or Author]
# 	eg  budget_mgmt.py search "Jesse" --by="title"
# 	 """
# 	click.secho("Searched For :: {}".format(number),bg='blue')
# 	from terminaltables import AsciiTable
# 	if by == 'Shop_id':
# 		result = get_note_by_Shop_id(number)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)
# 	elif by == 'author':
# 		result = get_note_by_author(number)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)
# 	elif by == 'message':
# 		result = get_note_by_msg(number)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)
# 	else:
# 		click.secho("{} Not a Choice ,Pls Try either of these [title/author/message]".format(by),bg='red')


# **************************************************************************************************************************

@main.command()
def show_all():
	""" Show All budget  
	
	eg. python budget_mgmt.py show-all
	"""
	click.secho("Showing All budget",bg='blue')
	click.echo("==============================")
	from terminaltables import AsciiTable
	result = view_all_budget()
	
	new_result = ['a_shop_id','a_month','a_budget_amount','a_amount_spent']
	click.secho('{}'.format(new_result),bg='blue')
	# click.secho('{}'.format(new_result),bg='blue')
	table1 = AsciiTable(result)
	click.echo(table1.table)



# ***************************
# def show_all():
#     	""" Show All Notes  
	
# 	eg. python termipad.py show-all
# 	"""
# 	click.secho("Showing All Notes",bg='blue')
# 	click.echo("==============================")
# 	from terminaltables import AsciiTable
# 	result = view_all_notes()
# 	new_result = ['Author','Title','Message']
# 	click.secho('{}'.format(new_result),bg='blue')
# 	table1 = AsciiTable(result)
# 	click.echo(table1.table)
# ******************************
	
# @main.command()
# @click.option('--old')
# @click.option('--new')
# @click.option('--field')
# def edit_note(field,old,new):
# 	""" Edit Note By Field[title/author/message] 
# 	eg. python budget_mgmt.py edit-note --field="author" --old="Jesse" --new="JCharis" 
# 	"""
# 	click.secho('Editing Field:: {} with {} and Updating to {}'.format(field,old,new),fg='yellow')
# 	from terminaltables import AsciiTable

# 	click.echo("===========Previous==============")
# 	result2 = view_all_budget()
# 	new_result = ['Author','Title','Message']
# 	click.secho('{}'.format(new_result),bg='blue')
# 	table2 = AsciiTable(result2)
# 	click.echo(table2.table)


# 	if field == 'title':
# 		result = edit_note_title(old,new)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)
# 	if field == 'author':
# 		result = edit_note_author(old,new)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)
# 	if field == 'message':
# 		result = edit_note_message(old,new)
# 		table1 = AsciiTable(result)
# 		click.echo(table1.table)


# 	click.echo("==========Updated===============")
# 	result3 = view_all_budget()
# 	new_result2 = ['Author','Title','Message']
# 	click.secho('{}'.format(new_result2),bg='blue')
# 	table3 = AsciiTable(result3)
# 	click.echo(table3.table)



# @main.command()
# @click.option('--title')
# def delete_note(title):
# 	""" Delete Note By Title 
# 	eg. python terminote.py delete-note --title "Best budget"
# 	"""
# 	click.secho('Deleting :: {} '.format(title),fg='yellow')
# 	from terminaltables import AsciiTable

# 	click.echo("===========Previous==============")
# 	result2 = view_all_budget()
# 	new_result = ['Author','Title','Message']
# 	click.secho('{}'.format(new_result),bg='blue')
# 	table2 = AsciiTable(result2)
# 	click.echo(table2.table)

# 	result = delete_data(title)
# 	click.echo("Deleted From DataBase")

# @main.command()
# def info():
# 	""" Show Info About Software 
	
# 	eg, python budget_mgmt.py info
# 	"""


# 	click.secho('Name:: {}'.format('Termipad'),bg='red')
# 	click.secho('Version:: {}'.format('0.01'),bg='yellow')
# 	click.secho('Motto:: {}'.format('Jesus Saves@JCharisTech'),bg='green')
# 	click.secho('Author:: {}'.format('Jesse E Agbe(JCharis)'),bg='blue')



if __name__ == '__main__':
	main()