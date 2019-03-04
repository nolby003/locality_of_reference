
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
        least_frequently_used()
    elif option == 2:
        least_recently_used()
    elif option == 3:
        longest_resident()
    elif option == 4:
        abort()            

    return

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

def least_frequently_used():

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
