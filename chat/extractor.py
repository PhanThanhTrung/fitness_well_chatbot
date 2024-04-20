#%%
import json
sample = [
    "Cảm ơn bạn đã cung cấp đầy đủ thông tin. Dựa trên mục tiêu tăng cơ và khả năng tập luyện 4 lần một tuần tại phòng gym của bạn, dưới đây là lịch tập mà tôi đề xuất:\n\n**DƯỚI ĐÂY LÀ LỊCH TẬP**\n\n- **Thứ 2: Ngày chân**\n    - **Squat:**\n        - Số lượng set: 4 (set)\n        - Số lượng rep: 8-10 (rep/set)\n        - Khối lượng tạ: 75% (1RM)\n        - Thời gian nghỉ: 90 (giây)\n    - **Leg Press:**\n        - Số lượng set: 3 (set)\n        - Số lượng rep: 10-12 (rep/set)\n        - Khối lượng tạ: 70% (1RM)\n        - Thời gian nghỉ: 90 (giây)\n    - **Calf Raises:**\n        - Số lượng set: 4 (set)\n        - Số lượng rep: 15 (rep/set)\n        - Thời gian nghỉ: 60 (giây)\n\n- **Thứ 4: Ngày tay và vai**\n    - **Bench Press:**\n        - Số lượng set: 4 (set)\n        - Số lượng rep: 8-10 (rep/set)\n        - Khối lượng tạ: 75% (1RM)\n        - Thời gian nghỉ: 90 (giây)\n    - **Military Press:**\n        - Số lượng set: 3 (set)\n        - Số lượng rep: 8-10 (rep/set)\n        - Khối lượng tạ: 70% (1RM)\n        - Thời gian nghỉ: 90 (giây)\n    - **Tricep Dips:**\n        - Số lượng set: 3 (set)\n        - Số lượng rep: 12 (rep/set)\n        - Thời gian nghỉ: 60 (giây)\n\n- **Thứ 6: Ngày lưng và lưng dưới**\n    - **Deadlift:**\n        - Số lượng set: 4 (set)\n        - Số lượng rep: 6-8 (rep/set)\n        - Khối lượng tạ: 80% (1RM)\n        - Thời gian nghỉ: 120 (giây)\n    - **Pull-Ups:**\n        - Số lượng set: 3 (set)\n        - Số lượng rep: 8-10 (rep/set)\n        - Thời gian nghỉ: 90 (giây)\n    - **Bent Over Row:**\n        - Số lượng set: 3 (set)\n        - Số lượng rep: 10-12 (rep/set)\n        - Khối lượng tạ: 70% (1RM)\n        - Thời gian nghỉ: 90 (giây)\n\n- **Thứ 7: Ngày toàn thân năng động**\n    - **Circuit Training (gồm các bài tập như lunges, plank, jumping jacks):**\n        - Lặp lại mỗi bài 3 vòng\n        - Thời gian mỗi bài: 1 phút\n        - Thời gian nghỉ giữa các vòng: 60 (giây)\n\n**KẾT THÚC LỊCH TẬP**\n\nVui lòng đảm bảo khởi động kỹ trước khi tập và làm mát cơ thể sau khi tập để tránh chấn thương. Chúc bạn tập luyện hiệu quả!"
]
#%%
def _contain_workout_schedule(message):
    pattern = "DƯỚI ĐÂY LÀ LỊCH TẬP"
    if pattern in message:
        return True
    return False

#%%
def __preprocess_ms(message):
    start_pattern = "**DƯỚI ĐÂY LÀ LỊCH TẬP**"
    end_pattern = "**KẾT THÚC LỊCH TẬP**"
    workout_schedule_str = message.split(start_pattern)[-1].split(end_pattern)[0]
    splitted_ws_str = workout_schedule_str.split("\n")
    splitted_ws_str = [elem for elem in splitted_ws_str if elem != '']
    return splitted_ws_str

def __normalize_txt(textline):
    textline = textline.strip()
    textline = textline.strip("- ")
    textline = textline.strip("**")
    textline = textline.replace("**", "")
    return textline

def __merge_all_line_to_days(all_schedule_line):
    elemental_day, all_days = [], []
    for textline in all_schedule_line:
        normed_textline = __normalize_txt(textline=textline)
        if normed_textline.startswith("Thứ ") and len(elemental_day)!=0:
            all_days.append(elemental_day)
            elemental_day = []
        elemental_day.append(normed_textline)
    return all_days

def __parse_to_json(schedule_str):
    day_title = schedule_str[0]
    

def _segmentize_message_to_days(message):
    all_schedule_line = __preprocess_ms(message=message)
    schedule_str_list = __merge_all_line_to_days(all_schedule_line=all_schedule_line)
# %%
