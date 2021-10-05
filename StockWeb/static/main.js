
function show_company(a){
    var text = document.querySelectorAll('.company_name');
    for(var i=0; i<100; i++){
        if(i==a){
            text[i].style.color='#FF8E66';
        }
        else{
            text[i].style.color='#615b54';
        }
    }
    
}

function show_rank(){
    text=[];
    company=['일진머티리얼즈',
    'SK텔레콤',
    '삼성에스디에스',
    '한온시스템',
    '신풍제약',
    '삼성증권',
    '한국전력',
    '현대모비스',
    '금호석유',
    '롯데케미칼',
    'SKC',
    'HMM',
    '한화솔루션',
    '고려아연',
    '현대미포조선',
    '삼성중공업',
    '한국조선해양',
    '삼성전기',
    'LG이노텍',
    '한미사이언스',
    'S-Oil',
    '호텔신라',
    'DB손해보험',
    '메리츠증권',
    'GS리테일',
    '삼성SDI',
    'POSCO',
    '미래에셋증권',
    'GS건설',
    '녹십자',
    'NH투자증권',
    '삼성전자',
    '현대제철',
    'LG',
    '포스코케미칼',
    '대한항공',
    '롯데지주',
    '쌍용C&E',
    '아모레G',
    '삼성화재',
    '현대차',
    '현대건설',
    'SK하이닉스',
    '기아',
    'CJ대한통운',
    '유한양행',
    '씨에스윈드',
    'KB금융',
    'SK이노베이션',
    'CJ제일제당',
    '아모레퍼시픽',
    '현대글로비스',
    '휠라홀딩스',
    'GS',
    '한국금융지주',
    '맥쿼리인프라',
    '셀트리온',
    'LG전자',
    '신한지주',
    '하나금융지주',
    'LG화학',
    'LG생활건강',
    '한국항공우주',
    '대우건설',
    '대우조선해양',
    '한국가스공사',
    '카카오',
    '엔씨소프트',
    'NAVER',
    '강원랜드',
    'LG디스플레이',
    'SK',
    '두산중공업',
    'LG유플러스',
    '삼성카드',
    'KT',
    '삼성물산',
    '팬오션',
    'KT&G',
    '삼성엔지니어링',
    '기업은행',
    '삼성생명',
    '코웨이',
    '하이브',
    'SK바이오팜',
    '현대오토에버',
    '우리금융지주',
    'SK바이오사이언스',
    'F&F',
    '현대중공업지주',
    '효성티앤씨',
    'SK아이이테크놀로지',
    '오리온',
    '넷마블',
    '삼성바이오로직스',
    '한미약품',
    '한국타이어앤테크놀로지',
    '이마트',
    '한진칼',
    '두산밥캐'];

    b = ['+','-'];
    c = ['12','9'];
    for(var i=0; i<100; i++)
    {
        if(i%2==0){
            text+=`<div class='rank_box' onclick="show_company(${i})" ><p class='number'>${i+1}</p><p class='company_name'>${company[i]}</p><p class="percent" style='color: red;'>${b[0]}${c[0]}%</p></div>`;
        }
        else{
            text+=`<div class='rank_box' onclick="show_company(${i})" ><p class='number'>${i+1}</p><p class='company_name'>${company[i]}</p><p class="percent" style='color: blue;'>${b[1]}${c[1]}%</p></div>`;
        }
        
    }
    document.querySelector('.select_box').innerHTML = text;
}

show_rank();


// 이상치 갯수 들어올 변수
let anomaly_num=10;

function make_button(){

    colors_button=[
        '#9CFF8F',
        '#B2E882',
        '#E8E382',
        '#FFEE8F',
        '#4E8047',
        '#DFFFDB',
        '#70806E',
        '#7DCC72',
        '#B6C867',
        '#9CFFCA',
        '#E8FF82']
    text3=[];
    for(var i=0; i<anomaly_num; i++){
        text3+=`<button class='anomaly_button' style="background-color:${colors_button[i]};">구간 ${i+1}</button>`;}
    document.querySelector('#button_box').innerHTML = text3;
}
make_button();

