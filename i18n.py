# -*- coding: UTF-8 -*-
import bpy

dict = {
    "en_US":{
        (None, "You need Blender 3.0+ to use this addon"):"You need Blender 3.0+ to use this addon",
        (None, "Select Vmd File"):"Select Vmd File",
        (None, "Select Avatar Type"):"Select Avatar Type",
        (None, "Select Model Type:"):"Select Model Type:",
        (None, "High Heel"):"High Heel",
        (None, "Check to ignore foot rotation"):"Check to ignore foot rotation",
        (None, "Body"):"Body",
        (None, "Check to import body motion"):"Check to import body motion",
        (None, "Must uncheck Rename bones when importing mmd model"):"Must uncheck Rename bones when importing mmd model",
        (None, "Upperarm"):"Upperarm",
        (None, "Forearm"):"Forearm",
        (None, "Shoulder"):"Shoulder",
        (None, "Set Arm's rotation rate"):"Set Arm's rotation rate",
        (None, "Only works when retargeting from vmd file"):"Only works when retargeting from vmd file",
        (None, "Eyeball"):"Eyeball",
        (None, "Check to import eyeball motion"):"Check to import eyeball motion",
        (None, "Facial"):"Facial",
        (None, "Check to import facial motion"):"Check to import facial motion",
        (None, "Viseme"):"Viseme",
        (None, "Check to import Viseme motion"):"Check to import Viseme motion",
        (None, "Interpolation type, does not affect on camera"):"Interpolation type, does not affect on camera",
        (None, "Easing type, does not affect on camera"):"Easing type, does not affect on camera",
        (None, "Check to import camera motion"):"Check to import camera motion",
        (None, "Rate"):"Rate",
        (None, "Camera Rate"):"Camera Rate",
        (None, "Height Offset(cm)"):"Height Offset(cm)",
        (None, "Move Up 8cm if model is on high heel"):"Move Up 8cm if model is on high heel",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"It gonna slow down the retargeting a lot, only check it when importing a pose",
        (None, "Nothing selected"):"Nothing selected",
        (None, "Pls select an Armature, mesh or camera"):"Pls select an Armature, mesh or camera",
        (None, "Check to import:"):"Check to import:",
        (None, "Arm Rotation Rate:"):"Arm Rotation Rate:",
        (None, "Or pick a MMD model as source:"):"Or pick a MMD model as source:",
        (None, "Easing:"):"Easing:",
        (None, "Camera Setting:"):"Camera Setting:",
        (None, "Debug Mode"):"Debug Mode",
        (None, "Execute"):"Execute",
        (None, "Combine Vmd and Mmd"):"Combine Vmd and Mmd",
        (None, "Use Vmd file's Upper body motion and Mmd model's lower body motion"):"Use Vmd file's Upper body motion and Mmd model's lower body motion",
        (None, "Set Position X's rate"):"Set Position X's rate",
        (None, "Position rate:"):"Position rate:",
        (None, "Object you selected is not an Armature"):"Object you selected is not an Armature",
        (None, "https://github.com/butaixianran/Blender-Vmd-Retargeting"):"https://github.com/butaixianran/Blender-Vmd-Retargeting",
        (None, "Document"):"Document",
        (None, "Feedback"):"Feedback",
        (None, "Use Vmd's Interpolation"):"Use Vmd's Interpolation",
        (None, "Arm Rotation Euler Plus:"):"Arm Rotation Euler Plus:",
        (None, "Forearm Left"):"Forearm Left",
        (None, "Forearm Right"):"Forearm Right",
        (None, "Found new version"):"Found new version",
        (None, "Use Thigh Rotation with IK"):"Use Thigh Rotation with IK",
        (None, "Thigh Rotation Rate"):"Thigh Rotation Rate",
    },
    "zh_CN":{
        (None, "You need Blender 3.0+ to use this addon"):"请使用Blender 3.0以上版本",
        (None, "Select Vmd File"):"选择vmd文件",
        (None, "Select Avatar Type"):"选择模型类型",
        (None, "Select Model Type:"):"选择模型类型:",
        (None, "High Heel"):"高跟鞋",
        (None, "Check to ignore foot rotation"):"勾选后无视脚踝旋转",
        (None, "Body"):"身体",
        (None, "Check to import body motion"):"勾选导入身体运动",
        (None, "Must uncheck Rename bones when importing mmd model"):"导入mmd模型时，必须取消勾选重命名骨骼",
        (None, "Upperarm"):"上臂",
        (None, "Forearm"):"前臂",
        (None, "Shoulder"):"肩膀",
        (None, "Set Arm's rotation rate"):"设置手臂旋转比例",
        (None, "Only works when retargeting from vmd file"):"只在从vmd文件导入时有效",
        (None, "Eyeball"):"眼球",
        (None, "Check to import eyeball motion"):"勾选导入眼球运动",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"勾选导入表情",
        (None, "Viseme"):"口型",
        (None, "Check to import Viseme motion"):"勾选导入口型",
        (None, "Interpolation type, does not affect on camera"):"补间曲线类型，不影响摄像机",
        (None, "Easing type, does not affect on camera"):"平滑过渡类型，不影响摄像机",
        (None, "Check to import camera motion"):"勾选导入摄像机运动",
        (None, "Rate"):"调整比例",
        (None, "Camera Rate"):"调整比例",
        (None, "Height Offset(cm)"):"高度偏移(cm)",
        (None, "Move Up 8cm if model is on high heel"):"模型有高跟鞋可上调8厘米",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"会明显拖慢转换过程，只在导入单个动作时启用",
        (None, "Nothing selected"):"没有选择导入任何东西",
        (None, "Pls select an Armature, mesh or camera"):"请选择一个骨骼，模型或摄像机",
        (None, "Check to import:"):"勾选导入:",
        (None, "Arm Rotation Rate:"):"手臂旋转比例:",
        (None, "Or pick a MMD model as source:"):"或选择一个mmd模型作为源:",
        (None, "Easing:"):"平滑过渡:",
        (None, "Camera Setting:"):"摄影机设置:",
        (None, "Debug Mode"):"调试模式",
        (None, "Execute"):"执行",
        (None, "Combine Vmd and Mmd"):"合并vmd和mmd动作",
        (None, "Use Vmd file's Upper body motion and Mmd model's lower body motion"):"使用vmd文件的上半身和mmd模型的下半身合并身体动作",
        (None, "Set Position X's rate"):"设置X轴移动的比例",
        (None, "Position rate:"):"移动比例:",
        (None, "Object you selected is not an Armature"):"你选择的对象不是骨架",
        (None, "https://github.com/butaixianran/Blender-Vmd-Retargeting"):"https://github.com/butaixianran/Blender-Vmd-Retargeting/blob/main/Readme.cn.md",
        (None, "Document"):"文档",
        (None, "Feedback"):"反馈",
        (None, "Use Vmd's Interpolation"):"使用Vmd的补间曲线",
        (None, "Arm Rotation Euler Plus:"):"手臂旋转欧拉角增量:",
        (None, "Forearm Left"):"左前臂",
        (None, "Forearm Right"):"右前臂",
        (None, "Found new version"):"找到新版本",
        (None, "Use Thigh Rotation with IK"):"大腿旋转和IK并用",
        (None, "Thigh Rotation Rate"):"大腿旋转比例",
    },
    "zh_TW":{
        (None, "You need Blender 3.0+ to use this addon"):"請使用Blender 3.0以上版本",
        (None, "Select Vmd File"):"選擇vmd文件",
        (None, "Select Avatar Type"):"選擇模型類型",
        (None, "Select Model Type:"):"選擇模型類型:",
        (None, "High Heel"):"高跟鞋",
        (None, "Check to ignore foot rotation"):"勾選後無視腳踝旋轉",
        (None, "Body"):"身體",
        (None, "Check to import body motion"):"勾選導入身體運動",
        (None, "Must uncheck Rename bones when importing mmd model"):"導入mmd模型時，必須取消勾選重命名骨骼",
        (None, "Upperarm"):"上臂",
        (None, "Forearm"):"前臂",
        (None, "Shoulder"):"肩膀",
        (None, "Set Arm's rotation rate"):"設置手臂旋轉比例",
        (None, "Only works when retargeting from vmd file"):"只在從vmd文件導入時有效",
        (None, "Eyeball"):"眼球",
        (None, "Check to import eyeball motion"):"勾選導入眼球運動",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"勾選導入表情",
        (None, "Viseme"):"口型",
        (None, "Check to import Viseme motion"):"勾選導入口型",
        (None, "Interpolation type, does not affect on camera"):"補間曲線類型，不影響攝像機",
        (None, "Easing type, does not affect on camera"):"平滑過渡類型，不影響攝像機",
        (None, "Check to import camera motion"):"勾選導入攝像機運動",
        (None, "Rate"):"調整比例",
        (None, "Camera Rate"):"調整比例",
        (None, "Height Offset(cm)"):"高度偏移(cm)",
        (None, "Move Up 8cm if model is on high heel"):"模型有高跟鞋可上調8厘米",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"會明顯拖慢轉換過程，只在導入單個動作時啟用",
        (None, "Nothing selected"):"沒有選擇導入任何東西",
        (None, "Pls select an Armature, mesh or camera"):"請選擇一個骨骼，模型或攝像機",
        (None, "Check to import:"):"勾選導入:",
        (None, "Arm Rotation Rate:"):"手臂旋轉比例:",
        (None, "Or pick a MMD model as source:"):"或選擇一個mmd模型作為源:",
        (None, "Easing:"):"平滑過渡:",
        (None, "Camera Setting:"):"攝影機設定:",
        (None, "Debug Mode"):"調試模式",
        (None, "Execute"):"執行",
        (None, "Combine Vmd and Mmd"):"合併vmd和mmd動作",
        (None, "Use Vmd file's Upper body motion and Mmd model's lower body motion"):"使用vmd文件的上半身和mmd模型的下半身合併身體動作",
        (None, "Set Position X's rate"):"設置X軸移動的比例",
        (None, "Position rate:"):"移動比例:",
        (None, "Object you selected is not an Armature"):"你選擇的對象不是骨架",
        (None, "https://github.com/butaixianran/Blender-Vmd-Retargeting"):"https://github.com/butaixianran/Blender-Vmd-Retargeting/blob/main/Readme.cn.md",
        (None, "Document"):"文檔",
        (None, "Feedback"):"回饋",
        (None, "Use Vmd's Interpolation"):"使用Vmd的補間曲線",
        (None, "Arm Rotation Euler Plus:"):"手臂旋轉歐拉角增量:",
        (None, "Forearm Left"):"左前臂",
        (None, "Forearm Right"):"右前臂",
        (None, "Found new version"):"找到新版本",
        (None, "Use Thigh Rotation with IK"):"大腿旋轉和IK並用",
        (None, "Thigh Rotation Rate"):"大腿旋轉比例",
    },
    "ja_JP":{
        (None, "You need Blender 3.0+ to use this addon"):"Blender 3.0以上を使用してください",
        (None, "Select Vmd File"):"Vmdファイルを選択",
        (None, "Select Avatar Type"):"アバターのタイプを選択",
        (None, "Select Model Type:"):"モデルのタイプを選択:",
        (None, "High Heel"):"ハイヒール",
        (None, "Check to ignore foot rotation"):"足首の回転を無視",
        (None, "Body"):"ボディ",
        (None, "Check to import body motion"):"ボディモーションをインポート",
        (None, "Must uncheck Rename bones when importing mmd model"):"mmdモデルを読み込むときは、[ボーンの名前を変更]をオフにする必要があります",
        (None, "Upperarm"):"腕",
        (None, "Forearm"):"ひじ",
        (None, "Shoulder"):"肩",
        (None, "Set Arm's rotation rate"):"腕の回転スケールを設定する",
        (None, "Only works when retargeting from vmd file"):"vmdファイルからのインポート時にのみ有効",
        (None, "Eyeball"):"目",
        (None, "Check to import eyeball motion"):"眼球モーションをインポート",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"表情モーションをインポート",
        (None, "Viseme"):"リップ",
        (None, "Check to import Viseme motion"):"リップモーションをインポート",
        (None, "Interpolation type, does not affect on camera"):"補間曲線を、カメラに影響なし",
        (None, "Easing type, does not affect on camera"):"スムーズタイプ、カメラに影響なし ",
        (None, "Check to import camera motion"):"カメラモーションをインポート",
        (None, "Rate"):"レート",
        (None, "Camera Rate"):"カメラレート",
        (None, "Height Offset(cm)"):"高さオフセット(cm)",
        (None, "Move Up 8cm if model is on high heel"):"ハイヒールをいるの場合は、8cm上に移動してください",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"読み込み速度が大幅に低下するため、1つのポーズを読み込む場合にのみ使用してください",
        (None, "Nothing selected"):"何も選択されていません",
        (None, "Pls select an Armature, mesh or camera"):"スケルトン、メッシュ、またはカメラを選択してください",
        (None, "Check to import:"):"チェックしてインポート:",
        (None, "Arm Rotation Rate:"):"腕の回転スケール:",
        (None, "Or pick a MMD model as source:"):"またはソースとしてmmdモデルを選択します:",
        (None, "Easing:"):"スムーズ:",
        (None, "Camera Setting:"):"カメラの設定:",
        (None, "Debug Mode"):"デバッグモード",
        (None, "Execute"):"実行",
        (None, "Combine Vmd and Mmd"):"vmdとmmdのマージ",
        (None, "Use Vmd file's Upper body motion and Mmd model's lower body motion"):"vmdファイルの上半身とmmdモデルの下半身を使用して体の動作をマージ",
        (None, "Set Position X's rate"):"X軸移動の割合を設定する",
        (None, "Position rate:"):"移動の割合:",
        (None, "Object you selected is not an Armature"):"選択したオブジェクトはスケルトンではありません",
        (None, "https://github.com/butaixianran/Blender-Vmd-Retargeting"):"https://github.com/butaixianran/Blender-Vmd-Retargeting",
        (None, "Document"):"ドキュメント",
        (None, "Feedback"):"フィードバック",
        (None, "Use Vmd's Interpolation"):"Vmdの補間曲線を使う",
        (None, "Arm Rotation Euler Plus:"):"腕の回転オーラル角の増分:",
        (None, "Forearm Left"):"左ひじ",
        (None, "Forearm Right"):"右ひじ",
        (None, "Found new version"):"新しいバージョンが見つかりました",
        (None, "Use Thigh Rotation with IK"):"足回転とIK併用",
        (None, "Thigh Rotation Rate"):"足回転の割合",
        
    },
}


def register():
    bpy.app.translations.register(__name__, dict)

def unregister():
    bpy.app.translations.unregister(__name__)

# need register
def word(msg_id):
    return bpy.app.translations.pgettext(msg_id)

# do not need register, but need to reboot blender
def word2(msg_id):
    lang = bpy.app.translations.locale
    msg_key = (None, msg_id)

    word = msg_id
    if lang in dict.keys():
        if msg_key in dict[lang].keys():
            word = dict[lang][msg_key]

    return word


