require 'colorize'

BEGIN {
   system("clear")
   require 'colorize'
   banner = system("python3 banner.py")
   puts(" ")
   sleep 1
   print("[+]".colorize(:cyan))
   sleep 0.2
   print(" ")
   puts("running console")
   puts(" ")
   sleep 2
   print("[+]".colorize(:cyan))
   sleep 0.2
   print(" ")
   puts("checking system")
   puts(" ")
   sleep 2
   print("[i]".colorize(:yellow))
   sleep 0.2
   print(" ")
   puts("-help for console help")
   sleep 2
}

konsole_ = "Q"
while konsole_ != "W"
   puts(" ")
   print "console >>>"
   input = gets.chomp
   if (input == "-help")
      puts("-v    console version
-s    support os
-u    update
-c    clear console
-e    exit
-ip   get ip")
   end

   if (input == "-v")
      puts(" ")
      print("[i] ".colorize(:yellow))
      print("Console Version ")
      puts("v0.9") 
   end
   if (input == "-c")
      system("clear")
   end
   if (input == "-e")
      exit 1
   end
   if (input == "-ip")
      puts(" ")
      print("[i] ".colorize(:yellow))
      print("IP Found  ")
      require 'socket'
      ip = Socket.ip_address_list.detect{|intf| intf.ipv4_private?}
      print(ip.ip_address)
      puts(" ")
   end
   if (input == "-s")
      platforms = ["Kali", "Debian", "Ubuntu", "Pop!_os", "Parrot OS"]
      puts(" ")
      print("[i] ".colorize(:yellow))
      print("Only Linux And Debian Base Support".colorize(:green))
      puts(" ")
      puts(" ")
      for i in platforms
         print("[+] ".colorize(:yellow))
         print(i)
         puts(" ")
      end
   end
end
