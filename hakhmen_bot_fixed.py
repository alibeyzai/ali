<!DOCTYPE html>
<html lang="fa">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>HAKHAMEN Clicker</title>
  <style>
    body {
      direction: rtl;
      margin: 0;
      font-family: Tahoma, sans-serif;
      background: linear-gradient(#0f0f0f, #1b1b1b);
      color: #f0e6d2;
      text-align: center;
      padding: 40px;
    }

    h1 {
      font-size: 2.5em;
      margin-bottom: 10px;
      color: #ffd700;
    }

    p {
      font-size: 1.2em;
      margin-bottom: 30px;
    }

    #score {
      font-size: 2em;
      margin: 20px 0;
      color: #00ffff;
    }

    .click-btn {
      background-color: #8b0000;
      border: none;
      padding: 20px 50px;
      font-size: 1.5em;
      border-radius: 15px;
      cursor: pointer;
      box-shadow: 0 0 20px #ff0000aa;
      transition: 0.2s ease-in-out;
    }

    .click-btn:hover {
      background-color: #aa0000;
      transform: scale(1.05);
    }

    .footer {
      margin-top: 40px;
      font-size: 0.9em;
      color: #aaa;
    }
  </style>
</head>
<body>
  <h1>:fire: HAKHAMEN Clicker :fire:</h1>
  <p>کلیک کن تا قدرت پنهان هخامنشی رو بیدار کنی!</p>
  <div id="score">امتیاز: ۰</div>
  <button class="click-btn" onclick="addScore()">کلیک کن</button>

  <div class="footer">ساخته‌شده توسط AB1ven ✦ توکن HKM</div>

  <script>
    let score = 0;

    function addScore() {
      score++;
      document.getElementById('score').innerText = "امتیاز: " + score;
    }
  </script>
</body>
</html>
