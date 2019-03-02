
#Locality of reference - page eviction algorithm for Cache in Operating systems - pythonic version
#author: Benjamin Nolan (nolby)
#completion date: 03/03/2019
#three types determined
#longest reisdent - longest page in all the frames will be replaced by the next page request
#least frequently used - the page that has been used the least with the lowest frequency
#least recently used - the page that has been recently used the least 

option = ''

def locality_of_reference():

    get_menu()

    return

def get_menu():

    #define what type of Locality of reference we want to determine
    #1: frequent
    #2: recent
    #3: longest 
    print('----------')
    print('Locality Of Reference - Python version')
    print('----------')
    print('MENU')
    print('----------')
    print('1 - Least Frequently Used')
    print('2 - Least Recently Used')
    print('3 - Longest resident')
    print('4 - Exit program')
    print('----------')
    
    option = int(input('Enter LOR type (1-4): '))

    while option not in range(1,5):
        print('\nInvalid choice, please enter either 1, 2, 3 or 4.\n')
        option = int(input('\nEnter LOR type (1-4): '))
    if option == 1:
        #least_frequenty_used_v1()
        #least_frequently_used_v2()
        least_frequently_used_v3()
    elif option == 2:
        least_recently_used()
        #least_frequently_used_v2()
    elif option == 3:
        longest_resident()
    elif option == 4:
        abort()            

    return

###WORKS##
def least_recently_used():

    cache = []
    page_requests = []

    num_frames = 3

    page = int(input('Enter page number to pass onto Cache: '))
    while page != -1:
    
        #captures every page into a list
        page_requests.append(page)   

        #need to fill in all frames
        if len(cache) < num_frames:
            #fill first frame at frame0 or f0
            if len(cache) == 0:
                #page at f0
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                #end
            #fill second frame at frame1 or f1
            elif len(cache) == 1:
                #page at f1
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                #end
            #fill third frame at frame2 or f2
            elif len(cache) == 2:
                #page at f2
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                #end
        #all three frames filled
        elif len(cache) == num_frames: 

            len_pages = len(page_requests)

            lastf0 = page_requests[len_pages-4]
            lastf2 = page_requests[len_pages-2]
            if lastf0 == lastf2:
                fifo = page_requests[len_pages-5] 
            else:
                fifo = page_requests[len_pages-4]    
            if page not in cache:

                index_frame = cache.index(fifo)
                cache[index_frame] = page

            print('Cache: ',cache)
            print('Page Requests: ',page_requests)

        page = int(input('\nEnter page number to pass onto Cache: '))

    return

###WORKS###
#Least Frequently Used - v3 FINAL
def least_frequently_used_v3():

    cache = []
    page_requests = []
    page_faults = []

    num_frames = 3

    page = int(input('Enter page number to pass onto Cache: '))
    while page != -1:
    
        #captures every page into a list
        page_requests.append(page)   

        #capture every page that is not equal to zero into page faults list
        if page != 0:
            page_faults.append(page)         

        #need to fill in all frames
        if len(cache) < num_frames:
            #fill first frame at frame0 or f0
            if len(cache) == 0:
                #page at f0
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                print('Page Faults: ',page_faults)
                #end
            #fill second frame at frame1 or f1
            elif len(cache) == 1:
                #page at f1
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                print('Page Faults: ',page_faults)
                #end
            #fill third frame at frame2 or f2
            elif len(cache) == 2:
                #page at f2
                cache.append(page)
                print('Cache: ',cache)
                print('Page Requests: ',page_requests)
                print('Page Faults: ',page_faults)
                #end
        #all three frames filled
        elif len(cache) == num_frames: 

            len_pages = len(page_requests)
            len_pf = len(page_faults)

            fifo = page_faults[len_pf-3]

            if page not in cache:

                index_frame = cache.index(fifo)
                cache[index_frame] = page

            print('Cache: ',cache)
            print('Page Requests: ',page_requests)
            print('Page Faults: ',page_faults)

        page = int(input('\nEnter page number to pass onto Cache: '))

    return

#attempt 2 - does not work
#Least Frequently Used - v2
def least_frequently_used_v2():

    cache = []
    page_count = [0,0,0]
    page_requests = []
    last_changes = []

    num_frames = 3
    
    page = int(input('Enter page number to pass onto Cache: '))
    while page != -1:
    
        #captures every page into a list
        page_requests.append(page)

        #need to fill in all frames
        if len(cache) < num_frames:
            #fill first frame at frame0 or f0
            if len(cache) == 0:
                #page at f0
                cache.append(page)
                #add page count to f0 of page_count list
                page_count[0] = 1
                print('Cache: ',cache)
                print('Count: ',page_count)
                #end
            #fill second frame at frame1 or f1
            elif len(cache) == 1:
                #page at f1
                cache.append(page)
                #add page count to f1 of page_count list
                page_count[1] = 1
                print('Cache: ',cache)
                print('Count: ',page_count)
                #end
            #fill third frame at frame2 or f2
            elif len(cache) == 2:
                #page at f2
                cache.append(page)
                #add page count to f2 of page_count list
                page_count[2] = 1
                print('Cache: ',cache)
                print('Count: ',page_count)
                #end
        #all three frames filled, which one is the longest? Should be f0 at this point
        #but below here should factor for all conditions
        elif len(cache) == num_frames: 
            #chg_frame = 0
            len_pages = len(page_requests)
            print('Len pages: ',len_pages)
            last_f0 = page_requests[len_pages-4]
            if last_f0 == 0:
                last_f0 = page_requests[len_pages-5]
                if last_f0 not in cache:
                    last_f0 = page_requests[len_pages-4]
                    last_f1 = page_requests[len_pages-3]
                    last_f2 = page_requests[len_pages-2]
                    print('foo1')
                else:     
                    last_f0 = page_requests[len_pages-5]
                    last_f1 = page_requests[len_pages-4]
                    last_f2 = page_requests[len_pages-3]
                    print('foo1.1')                    
                
            else:    
                last_f0 = page_requests[len_pages-4]
                last_f1 = page_requests[len_pages-3]
                last_f2 = page_requests[len_pages-2]
                print('foo2')
            print('Last F0: ',last_f0)
            print('Last F1: ',last_f1)
            print('Last F2: ',last_f2)
            last_three = [last_f0,last_f1,last_f2]
            print('Last three: ',last_three)

            if page not in cache:
            #    print('not in page')
            #    if page not in last_three and len_pages < 5:
            #        print('not in last three')
            #        print('total pages less than 5')
            #        chg_frame = 0
            #    elif page not in last_three and len_pages > 5:    
            #        print('not in last three')
            #        print('total pages greater than 5')
            #        if cache[2] in last_three:
            #            if cache[1] in last_three:
            #                if cache[0] in last_three:
            #                    chg_frame = 2
            #                elif cache[0] not in last_three:
            #                    chg_frame = 0
                            #endif
                        #endif         
                    #endif

                chg_frame = cache.index(last_f0)
                print('Change frame: ',chg_frame)

                cache[chg_frame] = page
                page_count[chg_frame] = 1
                print('Cache: ',cache)
                print('Count: ',page_count)               
            elif page in cache:
                print('Page in cache, updating page by 1')
                index_frame = cache.index(page)
                page_count[index_frame] = page_count[index_frame]+1
                print('Cache: ',cache)
                print('Count: ',page_count)
            #endif
        #endif
        print("Page requests: ",page_requests)
        page = int(input('\nEnter page number to pass onto Cache: '))
    #endwile        
    return

#attempt 1 - does not work
#Least Frequently Used - v1
def least_frequenty_used_v1():

    #define lists
    locref_set = []
    ind_list = []
    page_count = []
    page_reqs = []
    last_changes = []
    last_chg = []

    #define number of memory frames
    num_frames = 3

    #define frame variables
    f0 = 0
    f1 = 0
    f2 = 0
   
    ind_list = [f0,f1,f2]
    page_count = [f0,f1,f2]

    page = int(input('Enter page number to pass onto Cache: '))
    while page != -1:

        #captures every page
        page_reqs.append(page)

        #Fill in all frames           
        
        #first check if page list is less than 3, meaning we have not filled all 3 frames yet and need to do so       
        if len(locref_set) < 3:
            
            # we are at frame0    
            if len(locref_set) == 0: 
                
                #add page to frame0
                locref_set.append(page)
                
                #add first count for page at frame0
                page_count[0] = page_count[0]+1

                print('\n[Func 1.0: Frame0 filling]')                
                #print('Count: ',page_count)
                print('Cache: ',locref_set)
                print('Page requests: ',page_reqs)

            #we have frame0, need to fill in frame1
            elif len(locref_set) == 1:
                
                #Does page already exists?
                if page in locref_set:
                    
                    #get index position of page in page list
                    ind_page = locref_set.index(page)
                    
                    #add 1 to page count in count list
                    page_count[ind_page] = page_count[ind_page]+1

                    print('\n[Func 2.0: Frame1 filling if Page exists]')
                    #print('Count: ',page_count)
                    print('Cache: ',locref_set)
                    print('Page requests: ',page_reqs)
                
                #Page does not exist    
                else:
                    locref_set.append(page)
                    page_count[1] = page_count[1]+1

                    print('\n[Func 2.1: Frame1 filling if Page does not exist]')
                    #print('Count: ',page_count)
                    print('Cache: ',locref_set)
                    print('Page requests: ',page_reqs)
            
            #we have frame0 and frame1, need to fill in frame2
            elif len(locref_set) == 2:                   
                #Does page already exists?
                if page in locref_set:
                    #get index position of page in page list
                    ind_page = locref_set.index(page)
                    #add 1 to page count in count list
                    page_count[ind_page] = page_count[ind_page]+1

                    print('\n[Func 3.0: Frame2 filling if Page exists]')
                    #print('Count: ',page_count)
                    print('Cache: ',locref_set)
                    print('Page requests: ',page_reqs)
                    
                #Page does not exist    
                else:
                    locref_set.append(page)
                    page_count[2] = page_count[2]+1

                    print('\n[Func 3.1: Frame2 filling if Page does not exist]')
                    #print('Count: ',page_count)
                    print('Cache: ',locref_set)
                    print('Page requests: ',page_reqs)

            
        #All frames filled, now perform calc            
        
        #we now have all three frames filled, we now need to check least frequency used            
        elif len(locref_set) == 3:

            #WORKS    

            #Does page already exists?
            if page in locref_set:
                #get index position of page in page list
                ind_page = locref_set.index(page)
                #add 1 to page count in count list
                page_count[ind_page] = page_count[ind_page]+1

                print('\n[Func 4.0: we have three frames, if Page exists, count page]')

                #set last change
                if len(last_chg) <= 1:
                    last_chg.append(page)
                elif len(last_chg) >= 1 and len(last_chg) <= 2:
                    last_chg[0] = last_chg[1]
                    last_chg[1] = page    
                print('Last Page changes: ',last_chg)    

                #print('Count: ',page_count)
                print('Cache: ',locref_set)
                print('Page requests: ',page_reqs)
                
            #Page does not exist    
            else:

                #get lowest count    
                least_freq = min(page_count)
                #len_pages = len(page_reqs) #[7,0,1,2,0,3,0,4]
                #last_f2 = page_reqs[len_pages-2] #0
                #last_f1 = page_reqs[len_pages-3] #3
                #last_f0 = page_reqs[len_pages-4] #0
                #last_changes = [last_f0,last_f1,last_f2] #[0,3,0]

                #print('Least frequent',least_freq)

                #WORKS                   

                #if all frames equal same count then we swap frame0 [1,1,1] - frame0 is the least frequently used
                if page_count[0] == least_freq and page_count[1] == least_freq and page_count[2] == least_freq:
                    #set frame0 to page
                    locref_set[0] = page
                    #set count for frame0 to 0
                    page_count[0] = 1
                    print('\n[Func 4.1: Replace f0 based on all counts of all frames being 1]')

                    #set last change
                    if len(last_chg) <= 1:
                        last_chg.append(page)
                    elif len(last_chg) >= 1 and len(last_chg) <= 2:
                        last_chg[0] = last_chg[1]
                        last_chg[1] = page      
                    print('Last Page changes: ',last_chg)    

                else:

                    #DOES NOT  - most recent 
                    

                    #if page == last_changes[2] or page == last_changes[1] or page != last_changes[0]:
                    #    locref_set[0] = page
                    #    page_count[0] = 0
                    #elif page == last_changes[2] or page == last_changes[1] or page == last_changes[0]:
                    #    locref_set[0] = page
                    #    page_count[0] = 0
                    #elif page == last_changes[2] or page != last_changes[1] or page != last_changes[0]:
                    #    locref_set[0] = page
                    #    page_count[0] = 0
                    #else:
                    #    locref_set[2] = page
                    #    page_count[2] = 0  
                    #print('[Func4.2]')    
                
                    #BELOW WORKED slightly - suggest revert backc

                    #if frame0 and frame1 is equal to same count then change frame2 as frame0 is more likely recent and frame3 is most recent [1,1,0]
                    #if page_count[0] == least_freq and page_count[1] == least_freq:
                        #set frame1 to page
                    #    locref_set[1] = page
                        #set count for frame1 to 0
                    #    page_count[1] = 0
                    #if frame1 and frame2 is equal to same count then change frame0 as frame2 is more likely recent and frame1 is most recent [0,1,1]
                    #elif page_count[0] == 0 and page_count[1] == least_freq and page_count[2] == least_freq:
                        #set frame2 to page
                    #    locref_set[2] = page
                        #set count for frame2 to 0
                    #    page_count[2] = 0
                    #elif page_count[0] == 0 and page_count[1] != least_freq and page_count[2] != least_freq:
                        #set frame2 to page
                    #    locref_set[2] = page
                        #set count for frame2 to 0
                    #    page_count[2] = 0

                    #logical attempt #3
                    #pseudo
                    #we have three frames, a page in each frame, we have replaced frame0 on the 4th page request from [7,0,1] to [2,0,1]
                    #we then have a page reqeust already in frame1, so we count the existing page by 1 [2,0,1] 0 was 1 now is 2(count)
                    #we then have a new page request 3, 3 needs to go into the frame that was least frequently used
                    #7 was recently replaced by 2 on the 4th step
                    #0 was recently requested but existed and was counted up by one on the 5th step
                    #therefore the existing 1 will be replaced by the 3, therefore [2,0,3]

                    #should we look at the last two requests to determine which frame to swap out?
                    #page reqs = 7,0,1,2,0,3,0,4,2,3,0,3,2,1,2
                    #order should be:
                    #7,     7
                    #7,0    0    
                    #7,0,1  1
                    #2,0,1  2
                    #2,0,1  0
                    #2,0,3  3
                    #2,0,3  0
                    #4,0,3  4
                    #4,0,2  2
                    #3,0,2  3
                    #3,0,2  0
                    #3,0,2  3
                    #3,0,2  2
                    #3,0,1  1
                    #3,0,2  2


                
                    #last_changes = [last_f0,last_f1,last_f2] like [0,3,0]
                    #print('[Func4.2]') 
                #    print('Last changes: ',last_changes)
                    #if last_f2 in locref_set:
                    #    if last_f1 in locref_set:
                    #        print('Change index in Cache: ',chg_frame)
                    #        chg_frame = locref_set.index(last_f0)
                    #        locref_set[chg_frame] = page
                    #        page_count[chg_frame] = 1
                    
                    #changes frame0 @ 2,0,1 to 3,0,1 instead of 2,0,3
                    #if last_f2 in locref_set: #if most recent frame is in cache, go next
                    #    if last_f1 in locref_set: #if 2nd most recent frame is in cache, then match 3rd last frame (least frequently used) to cache and obtain index position of cache where value of 3rd last page is
                            #chg_frame = locref_set.index(last_f0)
                    #        chg_frame = 0
                    #elif last_f2 in locref_set:
                    #    if last_f0 in locref_set:
                    #        chg_feame = 1
                    #elif last_f1 in locref_set:
                    #    if last_f0 in locref_set:
                    #        chg_frame = 2

                    #if last_f2 in locref_set:
                    #    if page_count[0] == least_freq:
                    #        chg_frame = 0
                    #if last_f1 in locref_set:
                    #    if page_count[1] == least_freq:
                    #        chg_frame = 1
                    #if last_f0 in locref_set:
                    #    if page_count[2] == least_freq:
                    #        chg_frame = 2                                
                    
                    #if last_f2 in locref_set: #if 0 in [2,0,3] ,yes, go next
                    #    if last_f1 in locref_set: #if 3 in [2,0,3] ,yes, go next
                    #        if last_f0 in locref_set: #if 0 in [2,0,3] ,yes, change f0
                    #            chg_frame = 0                                        
                    
                    #if page_count[2] == least_freq: #if (1) == (1), then check if f2 in cache exists
                    #    if last_f2 in locref_set: #yes 0 exists
                    #        no_frame = last_f2 #0
                    #if page_count[1] == least_freq: #if (3) == (1), then check if f1 in cache exsts
                    #    if last_f1 in locref_set: #yes 3 exists
                    #        no_frame = last_f1
                    #if page_count[0] == least_freq: #if (1) == (1), then check if f0 in cache exists
                    #    if last_f0 in locref_set: #yes 3 exists
                    #        no_frame = last_f0

                    #0 == 3?    
                    #if last_f2 == locref_set[2]: 
                        #yes
                    #    if last_f1 == locref_set[2]:
                            #yes
                    #        if last_f0 == locref_set[0]:
                                #yes
                    #            chg_frame = 0
                    #no, 0 != 0    
                    #else: 
                        #if 0 == 0
                    #    if last_f2 == locref_set[1]: 
                            #yes, 0 == 0
                            #if 3 == 3
                    #        if last_f1 == locref_set[2]:
                                #yes, 3 == 3
                                #if 0 == 2
                    #            if last_f0 == locref_set[0]:
                                    #yes
                    #                return
                                #no, 0 != 2
                    #            else:
                    #                chg_frame = 0
                        #no
                    #    else:

                    #if locref_set[2] not in last_changes:
                    #    if locref_set[1] not in last_changes:
                    #        if locref_set[0] not in last_changes:
                    #            chg_frame = 2    
                    #else:
                    #    if locref_set[2] in last_changes:
                    #        if locref_set[1] in last_changes:
                    #            if locref_set[0] in last_changes:
                    #                chg_frame = 0 

                    #if page_count[2] == page_count[0]:
                    #    if locref_set[2] in last_changes:
                    #        if last_f0 == locref_set[2]:
                    #            chg_frame = 2
                    #        else:
                    #            chg_frame = 0 
                    #    elif locref_set[2] not in last_changes:
                    #        chg_frame = 2                                                 

                    # CLOSE TO BE PERFECT, JUST NEED TO GET LAST TWO CHANGE REFS RIGHT!

                    print('\n[Func 4.2: Change f0 or f2 based on least freq used (dependant on last two changes)]')

                    #set last change
                    if len(last_chg) <= 1:
                        last_chg.append(page)
                        print('[Func 4.21: append to last_chg]')
                    elif len(last_chg) >= 1 and len(last_chg) <= 2:
                        last_chg[0] = last_chg[1]
                        last_chg[1] = page
                        print('\n[Func 4.22: move last change to 2nd last and set last change to current page]')      
                    print('Last Page changes: ',last_chg)    

                    if locref_set[0] == last_chg[0]:
                        if locref_set[1] == last_chg[1]:
                            chg_frame = 2
                            #last_chg[0] = last_chg[1]
                            #last_chg[1] = page
                    elif locref_set[0] != last_chg[0]:
                        if locref_set[1] == last_chg[0]:        
                            if locref_set[2] == last_chg[1]:
                                chg_frame = 0
                                #last_chg[0] = last_chg[1]
                                #last_chg[1] = page                                

                    print('Change index in Cache: ',chg_frame)
                    locref_set[chg_frame] = page
                    page_count[chg_frame] = 1


                
                #print('Count: ',page_count)
                print('Cache: ',locref_set)
                print('Page requests: ',page_reqs)
                

        page = int(input('\nEnter page number to pass onto Cache: '))

    return


###WORKS###
#determine longest page in memory
#Longest resident
def longest_resident():    

    #define lists
    locref_set = []
    ind_list = []
    page_count = []
    page_reqs = []
    last_changes = []

    #define number of memory frames
    num_frames = 3

    #define frame variables
    f0 = 0
    f1 = 0
    f2 = 0
    
    ind_list = [f0,f1,f2]
    page_count = [f0,f1,f2]

    page = int(input('1Enter page number to pass onto Cache: '))
    while page != -1:

        print('\nCurrent Index list: ',ind_list) 
        longest = max(ind_list)
        print('Longest Page: ',longest)
        ind_page = ind_list.index(longest)
        print('Index page: ',ind_page)

        if len(locref_set) < 3:
            locref_set.append(page)
            if len(locref_set) == 1:
                ind_list[0] = ind_list[0]+1
                print('New Index list: ',ind_list)
            elif len(locref_set) == 2:
                ind_list[0] = ind_list[0]+1
                ind_list[1] = ind_list[1]+1
                print('New Index list: ',ind_list)
        elif len(locref_set) == 3:
            if page not in locref_set: 
                ind_list[0] = ind_list[0]+1
                ind_list[1] = ind_list[1]+1
                ind_list[2] = ind_list[2]+1
                print('New Index list: ',ind_list)
                locref_set[ind_page] = page
                ind_list[ind_page] = 0
        
        print('Cache: ',locref_set)
        page = int(input('\n2Enter page number to pass onto Cache: '))

    return    

# quit program 
def abort():

    print('Goodbye.')

if option not in range(1,5):
    get_menu()
    
#start program
locality_of_reference()

#EOF
