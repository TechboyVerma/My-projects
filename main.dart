import 'package:flutter/material.dart';
import 'PlayListPage.dart';
import 'ProfilePage.dart';
import 'SearchPage.dart';
import 'HomePage.dart';
void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int _courentTab = 0;
  final Tabs = [
    HomePage(),
    SearchPage(),
    PlayListPage(),
    ProfilePage(),
  ];
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SafeArea(
        child: Scaffold(
          backgroundColor: Colors.black,
          body: Tabs[_courentTab], //HomePage(),tabs[_courentTab],
          bottomNavigationBar: BottomNavigationBar(
            currentIndex: _courentTab,

            type: BottomNavigationBarType.shifting,
            items:[
              BottomNavigationBarItem(
                icon: Icon(Icons.home,color: Colors.white,),
                label: "Home",
                backgroundColor: Color.fromARGB(255, 20, 20, 20),
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.search,color: Colors.white,),
                label: "Search",
                backgroundColor: Color.fromARGB(255, 20, 20, 20),
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.library_music,color: Colors.white,),
               label: "Playlist",
                backgroundColor: Color.fromARGB(255, 20, 20, 20),
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.person,color: Colors.white,),
                label: "Profile",
                backgroundColor: Color.fromARGB(255, 20, 20, 20),

              ),

            ],
            onTap: (index){
              setState(() {
                _courentTab = index;
              });
            },
          ),
        ),
      ),

    );
  }
}
