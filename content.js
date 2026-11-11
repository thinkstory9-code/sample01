/*
 * 이 파일만 바꾸면 글과 사진을 수정할 수 있습니다.
 * - title: 페이지 제목 (\n 줄바꿈)
 * - body: 본문 (\n 줄바꿈, \n\n 문단 구분)
 * - caption: 사진 아래에 들어갈 글
 * - image: photos 폴더 안의 사진 파일 경로
 * - 페이지 추가/삭제: pages 배열의 { ... } 묶음 편집
 */
window.BOOKLET_CONTENT = {
  siteName: "마음이 흐린 날에",
  edition: "A LITTLE COMFORT · VOL. 01",
  footer: "마음이 흐린 날에 · 작은 쉼표",

  pages: [
    {
      kind: "cover",
      layout: "image-left",
      label: "COVER / 작은 위로의 시작",
      title: "마음이\n흐린 날에",
      body: "잠시 머물다 가도 괜찮아요.\n오늘의 당신에게 건네는 다섯 장의 조용한 위로.",
      image: "photos/cover-sunrise.webp",
      imageAlt: "엷은 분홍 구름 아래로 산 너머 떠오르는 아침 해",
      caption: "조용히 밝아오는 아침"
    },
    {
      kind: "story",
      layout: "image-right",
      label: "01 / 마음을 알아차리기",
      title: "괜찮지 않은\n날도 있어요",
      body: "이유 없이 마음이 가라앉는 날이 있어요.\n그런 날까지 씩씩할 필요는 없어요.\n\n지금의 마음을 억지로 바꾸지 않아도 괜찮아요.",
      image: "photos/rainy-window.webp",
      imageAlt: "빗방울이 맺힌 창문 앞에 놓인 머그잔과 책",
      caption: "비가 잠시 머무는 창가"
    },
    {
      kind: "story",
      layout: "image-left",
      label: "02 / 잠깐의 쉼",
      title: "잠시 멈춰도\n괜찮아요",
      body: "해야 할 일은 잠깐 내려놓고,\n따뜻한 차 한 모금부터 마셔봐요.\n\n아무것도 하지 않는 시간에도\n당신의 하루는 흘러가고 있어요.",
      image: "photos/warm-tea.webp",
      imageAlt: "비 오는 창가에서 김이 오르는 따뜻한 찻잔",
      caption: "따뜻한 한 잔이 있는 오후"
    },
    {
      kind: "story",
      layout: "image-right",
      label: "03 / 작은 한 걸음",
      title: "오늘은\n한 걸음만",
      body: "멀리까지 보지 않아도 돼요.\n창문을 열고 바람을 느끼는 일,\n잠깐 밖을 걷는 일.\n\n지금 가능한 작은 한 가지면 충분해요.",
      image: "photos/forest-path.webp",
      imageAlt: "나뭇잎 사이로 햇빛이 비치는 고요한 숲길",
      caption: "햇빛이 닿는 작은 숲길"
    },
    {
      kind: "ending",
      layout: "image-left",
      label: "END / 당신에게",
      title: "조금은 가벼운\n내일이기를",
      body: "모든 것이 곧 괜찮아질 거라고\n쉽게 말하지 않을게요.\n\n다만, 무거운 마음을 혼자 견디지 않아도 돼요.\n필요할 때는 누군가에게 기대어도 괜찮아요.\n\n이 페이지가 잠깐의 쉼이 되기를.",
      image: "photos/sunlit-meadow.webp",
      imageAlt: "연한 햇살 속에서 작은 들꽃이 피어 있는 풀밭",
      caption: "빛이 머무는 작은 들판"
    }
  ]
};
