def solution(name, yearning, photo):
    answer = []
    
    # 추억 점수를 매기기
    # 사진 속 인물의 그리움 점수를 모두 더하면 해당 사진의 추억 점수
    
    for ppl in photo:
        score=0
        for n in ppl:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
        
        
    return answer