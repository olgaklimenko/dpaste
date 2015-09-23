function getBlockFromEvent (evt) {
// создание range в месте, где происходит событие, расширение range до блока. Возвращаем текст из range
    if (evt.rangeParent && document.createRange) {
        var range = document.createRange();
        range.setStart(evt.rangeParent, evt.rangeOffset);
        range.setEnd(evt.rangeParent, evt.rangeOffset);
        expandRangeToBlock(range);
        var block = range.toString();
        range.detach();
        return block;    
    }
    else {
        return null;
    }
}

function expandRangeToBlock (range) {
//расширяем границы range до блока текста, который находится внутри {}, выделяем этот блок.
  var startOfBlock = /{/m;
  var endOfBlock = /}/m;

  while (!startOfBlock.test(range.toString())) {
    range.setStart(range.startContainer, range.startOffset - 1);
  }
  range.setStart(range.startContainer, range.startOffset);
  while (!endOfBlock.test(range.toString())) {
    range.setEnd(range.endContainer, range.endOffset + 1);
  }
  range.setEnd(range.endContainer, range.endOffset);
  var selection;
  selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
  return range.toString();
}

function isMouseLeave (node, evt) {
if (evt.relatedTarget) {
    window.getSelection().removeAllRanges();
    return !contains(node, evt.relatedTarget);
  }
}

function contains (container, containee) {
  do {
    if (container == containee) {
      return true;
    }
    containee = containee.parentNode;
  }
  while (containee)
  return false;
}
