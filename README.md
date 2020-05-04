# how to use the library
# {
describe : pw_miniproject().describe(),

bnf_names : pw_miniproject().feature_name_list(),

group : pw_miniproject().group_by_feature().group 

max_item : pw_miniproject().group_by_feature().max_item(),

'challenge 1' group_by_field : pw_miniproject().group_by_field().group

test_max_item : pw_miniproject().group_by_field().test_max_term()

practice_postal :pw_miniproject().finding_practice_with_prescription()['K82019']

'challenge 2' practice_postal_with_group : pw_miniproject().group_by_field(dataset=practices,fields=('code',)).finding_prac_with_script_using_group_by_field()

joined : pw_miniproject(dataset=scripts).join_practice_and_prescription()

item_by_post : pw_miniproject().group_by_field(dataset=joined,fields=('post_code',)).list_test_max_item()

postal_totals : item_by_post
total_items_by_bnf_post : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_bnf_post(micro_attribute='bnf_name')

total_items_by_post : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_bnf_post()

max_item_by_post : :)

items_by_region : pw_miniproject().group_by_feature(dataset=joined,feature='post_code').items_by_region(micro_attribute='bnf_name')

# }"
