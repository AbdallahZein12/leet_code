class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """

        list_of_first_sent = s1.split()
        list_of_second_sent = s2.split()

        list_of_wrds = list_of_first_sent + list_of_second_sent 

        answer = list(map(lambda x: x if list_of_wrds.count(x)<2 else "", list_of_wrds))
        answer = [item for item in answer if item != ""]

        

        # list_of_first_sent = s1.split()
        # list_of_second_sent = s2.split()

        # unique_in_sent1 = []
        # for i in list_of_first_sent:
        #     if i in unique_in_sent1:
        #         unique_in_sent1.remove(i)
        #         list_of_first_sent = [item for item in list_of_first_sent if item != i]
        #     else:
        #         unique_in_sent1.append(i)
                
        # unique_in_sent2 = []
        # for i in list_of_second_sent:
        #     if i in unique_in_sent2:
        #         unique_in_sent2.remove(i)
        #         list_of_second_sent = [item for item in list_of_second_sent if item != i]
        #     else:
        #         unique_in_sent2.append(i)
        

        # if not unique_in_sent1:
        #     answer = unique_in_sent2

        # elif not unique_in_sent2:
        #     answer = unique_in_sent1
            
        # else:
        #     if len(unique_in_sent1) > len(unique_in_sent2):
        #         des_len = len(unique_in_sent1) - len(unique_in_sent2)
        #         des_len = [''] * des_len
        #         unique_in_sent2.extend(des_len)
        #     if len(unique_in_sent2) > len(unique_in_sent1):
        #         des_len = len(unique_in_sent2) - len(unique_in_sent1)
        #         des_len = [''] * des_len
        #         unique_in_sent1.extend(des_len)
            
                
        #     zipped_list = list(zip(unique_in_sent1,unique_in_sent2))

        #     answer = []

        #     for i in zipped_list:
        #         if i[0] != i[1]:
        #             answer.append(i[0])
        #             answer.append(i[1])
        # answer = [item for item in answer if item != ""]
        return answer 






# s1 = "s z z z s"
# s2 = "s z ejt"

# list_of_first_sent = s1.split()
# list_of_second_sent = s2.split()

# list_of_wrds = list_of_first_sent + list_of_second_sent

# answer = list(map(lambda x: x if list_of_wrds.count(x) < 2 else "", list_of_wrds))
# answer = [x for x in answer if x !='']

# print(answer)







# def uncommonFromSentences(s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: List[str]
#         """

#         list_of_first_sent = s1.split()
#         list_of_second_sent = s2.split()

#         unique_in_sent1 = []
#         for i in list_of_first_sent:
#             if i in unique_in_sent1:
#                 unique_in_sent1.remove(i)
#                 list_of_first_sent = [item for item in list_of_first_sent if item != i]
               
#             else:
#                 unique_in_sent1.append(i)
                
#         unique_in_sent2 = []
#         for i in list_of_second_sent:
#             if i in unique_in_sent2:
#                 unique_in_sent2.remove(i)
#                 list_of_second_sent = [item for item in list_of_second_sent if item != i]
#             else:
#                 unique_in_sent2.append(i)
#         print(unique_in_sent1)
#         print(unique_in_sent2)

#         if not unique_in_sent1:
#             answer = unique_in_sent2

#         elif not unique_in_sent2:
#             answer = unique_in_sent1
            
#         else:
#             if len(unique_in_sent1) > len(unique_in_sent2):
#                 des_len = len(unique_in_sent1) - len(unique_in_sent2)
#                 des_len = [''] * des_len
#                 unique_in_sent2.extend(des_len)
#             if len(unique_in_sent2) > len(unique_in_sent1):
#                 des_len = len(unique_in_sent2) - len(unique_in_sent1)
#                 des_len = [''] * des_len
#                 unique_in_sent1.extend(des_len)
            
                
#             zipped_list = list(zip(unique_in_sent1,unique_in_sent2))

#             answer = []

#             for i in zipped_list:
#                 if i[0] != i[1]:
#                     answer.append(i[0])
#                     answer.append(i[1])
#         answer = [item for item in answer if item != ""]
#         return answer 
    
    
# print(uncommonFromSentences("s z z z s","s z ejt"))