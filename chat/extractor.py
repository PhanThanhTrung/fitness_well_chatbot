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

#%%
def __normalize_txt(textline):
    textline = textline.strip()
    textline = textline.strip("- ")
    textline = textline.strip("**")
    textline = textline.replace("**", "")
    return textline

#%%
def __merge_all_line_to_days(all_schedule_line):
    elemental_day, all_days = [], []
    for textline in all_schedule_line:
        normed_textline = __normalize_txt(textline=textline)
        if normed_textline.startswith("Thứ ") and len(elemental_day)!=0:
            all_days.append(elemental_day)
            elemental_day = []
        elemental_day.append(normed_textline)
    if len(elemental_day) != 0:
        all_days.append(elemental_day)
    return all_days

#%%
def __mapping_days(input_str):
    _volcabulary = {
        "monday": ["thứ 2", "monday", "thứ hai", "ngày thứ hai", "ngày thứ 2"],
        "tuesday": ["thứ 3", "tuesday", "thứ ba", "ngày thứ ba", "ngày thứ 3"],
        "wenesday": ["thứ 4", "wenesday", "thứ tư", "ngày thứ tư", "ngày thứ 4"],
        "thusday": ["thứ 5", "thusday", "thứ năm", "ngày thứ năm", "ngày thứ 5"],
        "friday": ["thứ 6", "friday", "thứ sáu", "ngày thứ sáu", "ngày thứ 6"],
        "saturday": ["thứ 7", "saturday", "thứ bảy", "thứ bẩy", "ngày thứ bảy", "ngày thứ 7"],
        "sunday": ["chủ nhật", "thứ 8", "sunday", "thứ chủ nhật", "ngày chủ nhật", "ngày CN"],
    }
    for key, value in _volcabulary.items():
        if input_str in value:
            return key
    raise ValueError(f"Not found {input_str} in the volcabulary. Please give it a check")

#%%
def __get_exercise(input_list):
    exercise, output = {}, []
    for textline in input_list:
        if textline.endswith(':') and len(exercise)!=0:
            output.append(exercise)
            exercise = {}
        if textline.endswith(':'):
            exercise["name"] = textline.strip(':')
            continue
            
        if textline.startswith("Số lượng set:"):
            textline = textline.replace("Số lượng set: ", '')
            textline = textline.strip(' ')
            exercise["num_set"] = textline.split(' ')[0]
            exercise["num_set_unit"] = textline.split(' ')[1].strip('(').strip(')')
            continue
        
        if textline.startswith("Số lượng rep:"):
            textline = textline.replace("Số lượng rep: ", '')
            textline = textline.strip(' ')
            exercise["num_rep"] = textline.split(' ')[0]
            exercise["num_rep_unit"] = textline.split(' ')[1].strip('(').strip(')')
            continue
        
        if textline.startswith("Khối lượng tạ:"):
            textline = textline.replace("Khối lượng tạ: ", '')
            textline = textline.strip(' ')
            exercise["volume"] = textline.split(' ')[0]
            exercise["volume_unit"] = textline.split(' ')[1].strip('(').strip(')')
            continue

        if textline.startswith("Thời gian nghỉ:"):
            textline = textline.replace("Thời gian nghỉ: ", '')
            textline = textline.strip(' ')
            exercise["rest_per_set"] = textline.split(' ')[0]
            exercise["rest_per_set_unit"] = textline.split(' ')[1].strip('(').strip(')')
            continue

        if textline.startswith("Số lượng rep:"):
            textline = textline.replace("Số lượng rep: ", '')
            textline = textline.strip(' ')
            exercise["num_set"] = int(textline.split(' ')[0])
            exercise["num_set_unit"] = textline.split(' ')[1].strip('(').strip(')')
            continue
#%%
def __parse_to_json(schedule_str):
    day_title = schedule_str[0]
    try:
        weekday, main_muscle = day_title.split(': ')
    except Exception as e:
        # Miss identify line.
        print(f"Current value of day_title: {day_title}")
        raise e
    weekday = __mapping_days(input_str=weekday)
    main_muscle = main_muscle.split(',')
    output = {
        "day": weekday,
        "main_muscle": main_muscle,
    }
    return output
#%%
def _segmentize_message_to_days(message):
    all_schedule_line = __preprocess_ms(message=message)
    schedule_str_list = __merge_all_line_to_days(all_schedule_line=all_schedule_line)
# %%
