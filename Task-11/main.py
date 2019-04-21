import json


def main():
    data = {}
    sql = ''
    # sql_star = ''
    sql_binds = []
    sql_alter = []

    with open('test.json', 'r') as f:
        data = json.loads(f.read())
    schema = data["schemaName"]
    sql += f'DROP DATABASE IF EXISTS `{schema}`;\n'
    sql += f'CREATE DATABASE `{schema}`;\n'
    sql += f'USE `{schema}`;\n\n'
    
    
    for entity in data['entities']:
        for entity_key, entity_value in entity.items():
            sql += f'CREATE TABLE `{entity_key}` (\n'
            sql += f'id INT AUTO_INCREMENT NOT NULL,\n'
            for key, value in entity_value.items():
                if value[0] is '*': # list of objects
                    sql_tmp = ''
                    sql_tmp += f'CREATE TABLE {entity_key}_{value[1:]}_bind (\n'
                    sql_tmp += f'`{entity_key}` INT NOT NULL,\n'
                    sql_tmp += f'`{value[1:]}` INT NOT NULL,\n'
                    sql_tmp += f'FOREIGN KEY (`{entity_key}`) REFERENCES `{entity_key}`(id),\n'
                    sql_tmp += f'FOREIGN KEY (`{value[1:]}`) REFERENCES `{value[1:]}`(id)\n'
                    sql_tmp += f');\n'
                    sql_binds.append(sql_tmp)

                elif value == 'String':
                    sql += f'`{key}` VARCHAR(255) NOT NULL,\n'
                
                elif value == 'Number':
                    sql += f'`{key}` INT NOT NULL,\n'
                
                else: # foreign keys
                    sql_tmp = ''
                    sql_tmp += f'ALTER TABLE `{entity_key}`\n'
                    sql_tmp += f'ADD `{key}` INT NOT NULL,\n'
                    sql_tmp += f'ADD FOREIGN KEY (`{key}`) REFERENCES `{value}`(id);\n\n'
                    
                    sql_alter.append(sql_tmp)
            sql += 'PRIMARY KEY(id)\n'
            sql += ');\n\n'
      

    with open('database.sql', 'w') as sql_file:
        sql_file.write(sql)
        sql_file.write('\n'.join(sql_alter))
        sql_file.write('\n'.join(sql_binds))
        
    print(sql)

if __name__ == "__main__":
    main()
    