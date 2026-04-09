# Pinyin Punctuation Fixes Needed

Found 32 lines with incorrectly split compound words in HSK5 files.

## Summary by Problem Type

- **ér (儿/而)** suffix/conjunction incorrectly split: 25 cases
- **men (们)** plural suffix incorrectly split: 5 cases
- **shíhuà (实话)** split: 1 case
- **xīwàng (希望)** split: 1 case
- **yōushì (优势)** split: 1 case

---

## File: hsk5a_text_pinyin.md (14 problems)

### 1. Line 73
**Problem**: `wěi, ér` should be connected
**Chinese**: 一个评委要上前喊醒那个男的，女的却伸出手指做了个小声的动作，然后小心地从包里拿出纸笔，用左手歪歪扭扭写下一行字递给评委，而她的右肩一直让丈夫的脑袋靠着。
**Current Pinyin**: `...píng wěi, ér tā de...`
**Should be**: `...píng wěi, ér tā de...` (already correct - this is 而 "but/and")
**Action**: Check if this is actually a problem - 而 can be separated

### 2. Line 90
**Problem**: `men, ér`
**Chinese**: 但评委们还是决定先不催他们，而是再等待一段时间。
**Current Pinyin**: `...píng wěi men, ér shì...`
**Should be**: `...píng wěi men, ér shì...` (already correct - 而 is a conjunction)

### 3. Line 149
**Problem**: `wǒ, men` - should be `wǒmen` (我们 = we)
**Chinese**: 父亲悄悄把我拉到一边说："你妈说了，你还是留一串新房的钥匙给我们，要是我和你妈什么时候想来了，就来住上几天，顺便给你们晒晒被子，打扫打扫卫生。
**Current Pinyin**: `...gěi wǒ, men yào...`
**Should be**: `...gěi wǒmen, yào...`
**Action**: Remove comma between wǒ and men

### 4. Line 160
**Problem**: `chē, ér zi` - should be `chē, érzi` (儿子 = son)
**Chinese**: 下了长途车，儿子被冻得大哭。
**Current Pinyin**: `...cháng tú chē, ér zi bèi...`
**Should be**: `...cháng tú chē, érzi bèi...`
**Action**: Remove space between ér and zi

### 5. Line 580 (first instance)
**Problem**: `hǔ, ér` - 而 conjunction
**Chinese**: 没想到仔细一看，被射中的竟不是老虎，而是一块形状很像老虎的大石头，而且一整支箭几乎全都射到石头中去了！
**Current Pinyin**: `...lǎo hǔ, ér shì...`
**Should be**: Already correct - 而是 should be separated as `ér shì`

### 6. Line 580 (second instance)
**Problem**: `tou, ér` - 而且
**Action**: Already correct - 而且 should be `ér qiě`

### 7. Line 586
**Problem**: `le, ér` - 而
**Action**: Already correct

### 8. Line 622
**Problem**: `jiā, ér` - 而
**Action**: Already correct

### 9. Line 764
**Problem**: `zuì, ér` - 而且
**Action**: Already correct

### 10. Line 874
**Problem**: `bìng, ér` - 而
**Action**: Already correct

### 11. Line 1032
**Problem**: `gè, ér` - 而
**Action**: Already correct

### 12. Line 1183
**Problem**: `shǐ, ér` - 而
**Action**: Already correct

### 13. Line 1186
**Problem**: `xiàng, ér` - 而非
**Action**: Already correct

### 14. Line 1283
**Problem**: `míng, ér` - 而
**Action**: Already correct

---

## File: hsk5b_text_pinyin.md (18 problems)

### 15. Line 87
**Problem**: `xíng, ér` - 而且
**Action**: Already correct

### 16. Line 197
**Problem**: `qǐng, ér` - 而
**Action**: Already correct

### 17. Line 322
**Problem**: `ér, ér` - 女儿，而
**Action**: Already correct - first 儿 is part of 女儿 (nǚ'ér), second is conjunction 而

### 18-22. Line 439 (MULTIPLE PROBLEMS - this line needs fixing!)
**Chinese**: "不管以后在哪儿，我都会继续用我的力量影响山里的孩子们，因为他们是国家的未来与希望。
**Current Pinyin**: `" bù guǎn yǐ hòu zài nǎ, ér wǒ dū huì jì xù yòng wǒ de lì liàng yǐng xiǎng shān lǐ de hái zi, men yīn wèi tā men shì guó jiā de wèi lái yǔ xī. wàng`

**Problems**:
- `nǎ, ér` should be `nǎ'er` or `nǎr` (哪儿 = where) - but next word is 我, so punctuation IS correct
- Actually looking at Chinese: "在哪儿，" - comma should be AFTER 儿! Current pinyin has it wrong.
- `zi, men` should be `zimen` (孩子们 = children)
- `xī. wàng` should be `xīwàng` (希望 = hope)

**Should be**: `" bù guǎn yǐ hòu zài nǎ'er, wǒ dū huì jì xù yòng wǒ de lì liàng yǐng xiǎng shān lǐ de háizimen, yīn wèi tā men shì guó jiā de wèi lái yǔ xīwàng.`

### 23-24. Line 734 (MULTIPLE PROBLEMS - needs fixing!)
**Chinese**: 面对并不乐观的就业形势，他压力很大："说实话，我觉得自己实在没什么优势。
**Current Pinyin**: `Miàn duì bìng bù lè guān de jiù yè xíng shì, tā yā lì hěn dà: " shuō shí, huà wǒ jué de zì jǐ shí zài méi shén me yōu. shì`

**Problems**:
- `shí, huà` should be `shíhuà` (实话 = truth/honestly)
- `yōu. shì` should be `yōushì` (优势 = advantage)

**Should be**: `Miàn duì bìng bù lè guān de jiù yè xíng shì, tā yā lì hěn dà: " shuō shíhuà, wǒ jué de zì jǐ shí zài méi shén me yōushì.`

### 25. Line 772
**Problem**: `zì, ér` - 而且
**Action**: Already correct

### 26. Line 1017
**Problem**: `shuǐ, ér` - 而
**Action**: Already correct

### 27. Line 1102
**Problem**: `qiáo, ér` - 而
**Action**: Already correct

### 28. Line 1105
**Problem**: `shāng, ér` - 而且
**Action**: Already correct

### 29. Line 1162
**Problem**: `máo, ér` - 而
**Action**: Already correct

### 30. Line 1187
**Problem**: `zào, ér` - 而且
**Action**: Already correct

### 31. Line 1204
**Problem**: `tiān, ér` - 而
**Action**: Already correct

### 32. Line 1355
**Problem**: `tā. men` should be `tāmen` (它们 = they/them)
**Chinese**: "我不知道花草们受我的照顾，感谢我不感谢，反正我要感谢它们。
**Current Pinyin**: `...gǎn xiè tā. men`
**Should be**: `...gǎn xiè tāmen.`

---

## ACTUAL FIXES NEEDED: Only 5 lines!

After analysis, most "ér" cases are the conjunction 而 which SHOULD be separated. Only these need fixing:

1. **Line 149 (hsk5a)**: `wǒ, men` → `wǒmen`
2. **Line 160 (hsk5a)**: `chē, ér zi` → `chē, érzi`
3. **Line 439 (hsk5b)**: Fix `nǎ, ér` → `nǎ'er,` AND `zi, men` → `zimen` AND `xī. wàng` → `xīwàng`
4. **Line 734 (hsk5b)**: Fix `shí, huà` → `shíhuà` AND `yōu. shì` → `yōushì`
5. **Line 1355 (hsk5b)**: `tā. men` → `tāmen.`

Total: 5 lines (with multiple fixes on 2 of them)
