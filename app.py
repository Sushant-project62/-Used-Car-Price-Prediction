<!DOCTYPE html>
<html>
<head>
  <title>Car Price Prediction</title>
  <style>
    body {
      background: url("https://axleaddict.com/.image/t_share/MTk4NTE5NTU3MDY3OTA4NTQ3/man-gives-tour-of-the-most-exclusive-car-dealership-in-the-country.jpg") no-repeat center center fixed;
      background-size: cover;
      font-family: Arial, sans-serif;
      color: white;
      text-align: center;
      padding-top: 50px;
    }

    .form-container {
      background: rgba(0, 0, 0, 0.6);
      padding: 20px;
      border-radius: 12px;
      display: inline-block;
    }

    select, input, button {
      padding: 10px;
      margin: 10px;
      border-radius: 8px;
      border: none;
    }

    button {
      background-color: red;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h2>Car Price Prediction</h2>
  <div class="form-container">
    <form action="/predict" method="post">
      <label>Company:</label><br>
      <select name="company">
        {% for company in companies %}
          <option value="{{ company }}">{{ company }}</option>
        {% endfor %}
      </select><br>

      <label>Car Model:</label><br>
      <select name="car_models">
        {% for model in car_models %}
          <option value="{{ model }}">{{ model }}</option>
        {% endfor %}
      </select><br>

      <label>Year:</label><br>
      <select name="year">
        {% for y in years %}
          <option value="{{ y }}">{{ y }}</option>
        {% endfor %}
      </select><br>

      <label>Fuel Type:</label><br>
      <select name="fuel_type">
        {% for fuel in fuel_types %}
          <option value="{{ fuel }}">{{ fuel }}</option>
        {% endfor %}
      </select><br>

      <label>Kilometers Driven:</label><br>
      <input type="text" name="kilo_driven"><br>

      <button type="submit">Predict</button>
    </form>
  </div>
</body>
</html>
