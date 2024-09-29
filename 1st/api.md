# CRUD API
1주차: RESTful API에 대해 학습하고 간단한 CRUD API(책 정보 생성하기, 책 목록 가져오기, 책 정보 읽기, 책 정보 갱신하기, 책 정보 삭제하기)를 설계해본다.

## 책 정보 생성하기
- URL   
` /books `
- Method   
` POST `
- Data Params   
    - Required :   
        `title[String] = 책이름`   
        `author[String] = 저자`
    - Optional :    
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`
    - example :
        ```
        {
            title : "유데미 백엔드 챌린지",
            author : "최하은",
            publishedDate : "20240929",
            publisher : "Udemy",
            price : 10000,
            genre : "IT",
            description : "crud API"
        }
        ```
- Success Response   
    - code : `201`
    - contend :   
        `status[Number] - status code`    

        `data[Object] : 생성된 책의 정보`   
        `id[Number] - book id`   
        `title[String] = 책이름`   
        `author[String] = 저자`   
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`
    - example :   
        ```
        {
            status: 201,
            data: {
                id : 1,
                title : "유데미 백엔드 챌린지",
                author : "최하은",
                publishedDate : "20240929",
                publisher : "Udemy",
                price : 10000,
                genre : "IT",
                description : "crud API"
            }
        }
        ```
- Error Response
   - contend :   
        `status[Number] - 에러 status code`  
        `error[Object] - 에러 정보`  
        `code[String] - 에러 코드`   
        `message[String] - 에러 메시지`   
    - example :   
        ```
        {
            status: 400,
            error: {
                  code: "BOOK_CREATION_FAILED",
                  message: "Failed to create book information"
            }
        }
        ```
## 책 목록 가져오기
- URL   
` /books `
- Method   
` GET `
- Query Parameters
    - Required :    
        `page[Number] - 페이지 번호 (기본값 : 1)`   
        `size[Number] - 한 페이지 당 책의 수 (기본값 : 10)`   
    - Optional :    
        `sort[string] - 정렬 기준 (ex: title)`   
        `direction[string] - 정렬 방향 (기본값 : asc)`   
        `genre[String] - 장르 필터링`   
- Success Response   
    - code : `200`
    - contend :   
        `status[Integer] - status code` 
            
        `data[Object] : 반환된 책 목록과 페이지 정보`   

        `books[List] : 반환된 책 목록`   
        `id[Number] - book id`   
        `title[String] = 책이름`   
        `author[String] = 저자`   
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`

        `page[Object] : 페이지네이션 정보`   
        `currentPage[Number] - 현재 페이지 번호`   
        `totalPages[Number] = 총 페이지 수`   
        `totalBooks[Number] = 총 책 수`   
        `pageSize[Number] - 한 페이지당 책의 수`   
    - example :   
        ```
        {
            status: 200,
            data: {
                books: [
                    {
                        id : 1,
                        title : "유데미 백엔드 챌린지",
                        author : "최하은",
                        publishedDate : "20240929",
                        publisher : "Udemy",
                        price : 10000,
                        genre : "IT",
                        description : "crud API"
                    }
                ],
                page: {
                    currentPage: 1,
                    totalPages: 1,
                    totalBooks: 1,
                    pageSize: 10
                }
            }
        }
        ```
- Error Response
   - contend :   
        `status[Integer] - 에러 status code`  
        `code[String] - 에러 코드`   
        `message[String] - 에러 메시지`   
    - example :   
        ```
        {
            error: {
                  status: 500,
                  code: "LIST_RETRIEVAL_FAILED",
                  message: "Failed to retrieve the list"
            }
        }
        ```
## 책 정보 읽기
- URL   
` /books/{bookId} `
- Method   
` GET `
- URL Params   
    - Required :   
        ` bookId[Number] - 조회할 책의 고유 ID`
    - Optional : `None`
- Success Response   
    - code : `200`
    - contend :   
        `status[Integer] - status code` 
            
        `data[Object] : 조회된 책의 정보`   
        `id[Number] - book id`   
        `title[String] = 책이름`   
        `author[String] = 저자`   
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`
    - example :   
        ```
        {
            status: 201,
            data: {
                id : 1,
                title : "유데미 백엔드 챌린지",
                author : "최하은",
                publishedDate : "20240929",
                publisher : "Udemy",
                price : 10000,
                genre : "IT",
                description : "crud API"
            }
        }
        ```
- Error Response
   - contend :   
        `status[Integer] - 에러 status code`  
        `code[String] - 에러 코드`   
        `message[String] - 에러 메시지`   
    - example :   
        ```
        {
            error: {
                  status: 404,
                  code: "BOOK_NOT_FOUND",
                  message: "Book not found"
            }
        }
        ```   
 
## 책 정보 갱신하기
- URL   
` /books/{bookId} `
- Method   
` PUT `
- URL Params   
    - Required :   
        ` bookId[Number] - 갱신할 책의 고유 ID`
    - Optional : `None`
- Data Params   
    - Optional :   
        `title[String] = 책이름`   
        `author[String] = 저자`   
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`
    - example :
        ```
        {
            title : "유데미 백엔드 챌린지2",
            author : "che",
            publishedDate : "20240930",
            publisher : "유데미",
            price : 20000,
            genre : "Web",
            description : "crud API specification"
        }
        ```
- Success Response   
    - code : `200`
    - contend :   
        `status[Integer] - status code` 
            
        `data[Object] : 갱신된 책의 정보`   
        `id[Number] - book id`   
        `title[String] = 책이름`   
        `author[String] = 저자`   
        `publishedDate[string] - 출판일 (형식: YYYYMMDD)`   
        `publisher[string] - 출판사`   
        `price[Number] - 가격`   
        `genre[String] - 책 장르`   
        `description[String] - 책 설명`
    - example :   
        ```
        {
            status: 200,
            data: {
                id : 1,
                title : "유데미 백엔드 챌린지2",
                author : "che",
                publishedDate : "20240930",
                publisher : "유데미",
                price : 20000,
                genre : "Web",
                description : "crud API specification"
            }
        }
        ```
- Error Response
   - contend :   
        `status[Integer] - 에러 status code`  
        `code[String] - 에러 코드`   
        `message[String] - 에러 메시지`   
    - example :   
        ```
        {
            error: {
                  status: 400,
                  code: "BOOK_UPDATE_INVALID_DATA",
                  message: "Invalid input data"
            }
        }
        ```   
 
## 책 정보 삭제하기
- URL   
` /books/{bookId} `
- Method   
` DELETE `
- URL Params   
    - Required :   
        ` bookId[Number] - 삭제할 책의 고유 ID`
    - Optional : `None`
- Success Response   
    - code : `200`
    - contend :   
        `status[Integer] - status code` 
    - example :   
        ```
        {
            status: 200
        }
        ```
- Error Response
   - contend :   
        `status[Integer] - 에러 status code`  
        `code[String] - 에러 코드`   
        `message[String] - 에러 메시지`   
    - example :   
        ```
        {
            error: {
                  status: 500,
                  code: "BOOK_DELETION_FAILED",
                  message: "Failed to delete book information"
            }
        }
        ```   
 