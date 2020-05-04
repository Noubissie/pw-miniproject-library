scripts = "hello"
practices="practices"
class pw_miniproject(object):
    
    def __init__(self,dataset=scripts,group=""):
        """this is help message"""
        self.dataset = dataset
        self.group=group
        

    def __repr__(self):
        return "{\n\
                    describe : pw_miniproject().describe,\n\
                    \n\
                    bnf_names : pw_miniproject().feature_name_list(),\n\
                    \n\
                    group : pw_miniproject().group_by_feature\n\
                    \n\
                    max_item : pw_miniproject().group_by_feature().max_item(),\n\
                    \n\
                    'challenge 1' group_by_field : pw_miniproject().group_by_field().group\n\
                    \n\
                    test_max_item : pw_miniproject().group_by_field().test_max_term()\n\
                    \n\
                    practice_postal :pw_miniproject().finding_practice_with_prescription()['K82019']\n\
                    \n\
                    'challenge 2' practice_postal_with_group : pw_miniproject().group_by_field(dataset=practices,fields=('code',)).finding_prac_with_script_using_group_by_field()\n\
                    \n\
                    joined : pw_miniproject(dataset=scripts).join_practice_and_prescription()\n\
                    \n\
                    item_by_post : pw_miniproject().group_by_field(dataset=joined,fields=('post_code',)).list_test_max_item()\n\
                    \n\
                    postal_totals : item_by_post\n\
                    total_items_by_bnf_post : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_bnf_post(micro_attribute='bnf_name')\n\
                    \n\
                    total_items_by_post : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_bnf_post()\n\
                    \n\
                    max_item_by_post : :)\n\
                    \n\
                    items_by_region : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_region(micro_attribute='bnf_name')\n\
                    \n\
                   }"

        
    # Question 1: summary_statistics
    
    @staticmethod
    def describe(key):
        """describe : pw_miniproject().describe """
        key_list=sorted(map(lambda x: x[key],scripts))
        key_list_length = len(key_list)
        total = sum(key_list)
        avg = total/key_list_length
        s = (sum([(x-avg)**2 for x in key_list])/key_list_length)**0.5

        q25_term = (1/4)*(key_list_length+1)
        q25 = key_list[q25_term] if (key_list_length+1)%4==0 else (key_list[int(q25_term)]+key_list[int(q25_term)+1])/2

        q50_term = (1/2)*(key_list_length+1)
        med = key_list[q50_term] if (key_list_length+1)%2==0 else (key_list[int(q50_term)]+key_list[int(q50_term)+1])/2

        q75_term = (3/4)*(key_list_length+1)
        q75 = key_list[q75_term] if (key_list_length+1)%4==0 else (key_list[int(q75_term)]+key_list[int(q75_term)+1])/2


        return (total, avg, s, q25, med, q75)
    
    
    # Question 2: most_common_item
    
    
    def feature_name_list(self,feature="bnf_name"): #bnf_name
        """bnf_names : pw_miniproject().feature_name_list()"""
        """group : pw_miniproject().group_by_feature"""
        key_list=list(map(lambda x: x[feature],self.dataset))
        return list(set(key_list))
    
    
    @classmethod
    def group_by_feature(cls,dataset=scripts,feature="bnf_name"): #group_by_attribute
        cls_dataset = cls(dataset=dataset)
        feature_names = cls.feature_name_list(cls_dataset,feature)

        groups = {name: [] for name in feature_names}
        for script in cls_dataset.dataset:
            groups[script[feature]].append(script)

        return cls(dataset=dataset, group=groups)
    
 
    def max_item(self):
        """max_item : pw_miniproject().group_by_feature().max_item()"""
        lname=""
        length=0
        for key in self.group:
            values = 0
            for value in self.group[key]:
                values += value['items']
            if values>length:
                lname=key
                length=values
        return [(lname,length)] 
    
    
    # Question 3: postal_totals
    @classmethod
    def group_by_field(cls,dataset=scripts,fields=('bnf_name',)):
        cls_dataset = cls(dataset=dataset)

        groups = {field: [] for field in fields}
        for field in fields:
            micro_groups = {name: [] for name in cls.feature_name_list(cls_dataset,feature=field)}
            for feature in cls_dataset.dataset:
                micro_groups[feature[field]].append(feature)
            groups[field].append(micro_groups)

        return cls(dataset=dataset,group=groups)
    
   
    def test_max_term(self):
        lname=""
        length=0
        for field_key in self.group:
            for key in self.group[field_key][0]:
                values = 0
                for value in self.group[field_key][0][key]:
                    values += value['items']
                if values>length:
                    lname=key
                    length=values
        return [(lname,length)]
    
    
    @staticmethod
    def finding_practice_with_prescription(practices=practices,scripts=scripts):
        practices = sorted(practices,key=lambda x: x['post_code'],reverse=True)
        practice_postal = {script['practice']:"" for script in scripts}
        for practice in practices:
            if practice['code'] in practice_postal:
                practice_postal[practice['code']] = practice['post_code']
            else:
                practice_postal[practice['code']] = "no_prescription"
        return practice_postal
        
    
    # use with group_by_field
    def finding_prac_with_script_using_group_by_field(self,fields=('code',),search_value='K82019',feature_search='post_code',sort_by='post_code'):
        return sorted(self.group['code'][0][search_value],key=lambda x :x[sort_by])[0][feature_search]
    
    
    def join_practice_and_prescription(self):
        joined = self.dataset[:]
        a=self.finding_practice_with_prescription()
        for script in joined:
            script['post_code'] = a[script['practice'] ]
        return joined 
    
    #use with group by field
    def list_test_max_item(self):
        return_value =[]
        for field_key in self.group:
            for key in self.group[field_key][0]:
                if key != "no_prescription":
                    lname=""
                    length=0
                    values = 0
                    for value in self.group[field_key][0][key]:
                        values += value['items']
                    if values>length:
                        lname=key
                        length=values
                    return_value.append((lname,length))
        return sorted(return_value,key=lambda x:x[0])[:100]
    
    
    #Question 4: items_by_region
    
    #use with group by feature
    def items_by_bnf_post(self,variable='items',micro_attribute=None):
        return_value =[]
        for field_key in self.group: # {'post_code':[]}
            field_group_list = self.group[field_key]
            if field_key != "no_prescription":
                if micro_attribute == None:
                    return_value.append((field_key))
                else:
                    cls_dataset=self.group_by_feature(dataset=field_group_list,feature=micro_attribute) #new_group creation
                    
                    max_bnf_name = ""
                    for attribute_key in cls_dataset.group: #{buf_name:[]}

                        return_value.append((field_key,attribute_key))


        return sorted(set(return_value),key=lambda x:x[0])
    
    
    #use with group_by_feature
    def items_by_region(self,variable='items',micro_attribute=None):
        return_value =[]
        for field_key in self.group: # {'post_code':[]}

            total_items = 0
            max_bnf_name = ""
            max_item_value = 0
            field_group_list = self.group[field_key]

            if field_key != "no_prescription":
                if micro_attribute == None:
                    return_value.append((field_key))
                else:
                    new_group = self.group_by_feature(dataset=field_group_list,feature=micro_attribute).group
                    sorted_new_group = sorted(new_group)
                    for attribute_key in sorted_new_group: #{buf_name:[]}
                        indiv_item=0
                        for value in new_group[attribute_key]:
                            total_items += value[variable]
                            indiv_item +=value[variable]
                            if indiv_item >max_item_value:
                                max_bnf_name = attribute_key
                                max_item_value = indiv_item
                    return_value.append((field_key,max_bnf_name,max_item_value/total_items))

        return sorted(set(return_value),key=lambda x:x[0])[:100]

print(pw_miniproject())
