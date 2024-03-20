def test_create_with_params(self):
    """Test create command with parameters"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd('create State name="California"')
        HBNBCommand().onecmd('create State name="Arizona"')
        HBNBCommand().onecmd('all State')
        self.assertIn("'name': 'California'", f.getvalue())
        self.assertIn("'name': 'Arizona'", f.getvalue())

        HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        HBNBCommand().onecmd('all Place')
        self.assertIn("'name': 'My little house'", f.getvalue())
        self.assertIn("'number_rooms': 4", f.getvalue())
        self.assertIn("'number_bathrooms': 2", f.getvalue())
        self.assertIn("'max_guest': 10", f.getvalue())
        self.assertIn("'price_by_night': 300", f.getvalue())
        self.assertIn("'latitude': 37.773972", f.getvalue())
        self.assertIn("'longitude': -122.431297", f.getvalue())

